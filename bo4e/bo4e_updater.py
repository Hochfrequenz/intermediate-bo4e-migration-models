"""
This script checks if the current BO4E version is up-to-date.
"""

import logging
import os
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Optional

import click
from black import main as black_main
from bo4e_generator.__main__ import generate_bo4e_schemas
from bost.__main__ import main as bost_main
from bost.pull import OWNER, REPO, resolve_latest_version
from dotenv import dotenv_values, set_key
from git import Repo
from github import Github
from isort.main import main as isort_main

PR_TARGET_OWNER = "Hochfrequenz"
PR_TARGET_REPO = "intermediate-bo4e-migration-models"
BO4E_SOURCE_OWNER = OWNER
BO4E_SOURCE_REPO = REPO
REPO_ROOT = Path(__file__).parents[1]
DOTENV_FILE = REPO_ROOT / "bo4e/tox.env"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def current_version() -> str:
    """
    Query the current version from the tox.env file.
    The version tag should have the same format as the github release tag.
    E.g. "v2.0.13-rc3"
    """
    config = dotenv_values(DOTENV_FILE)
    assert config["BO4E_VERSION"] is not None
    return config["BO4E_VERSION"]


@contextmanager
def catch_all_exceptions(
    log_level: int, error_msg: str, *msg_args: Any, exit_code: Optional[int] = None, **msg_kwargs: Any
):
    try:
        yield
    except Exception as error:
        logger.log(log_level, error_msg, *msg_args, exc_info=error, **msg_kwargs)
        if exit_code is not None:
            sys.exit(exit_code)


def rebuild_bo4e(version: str, context: click.Context) -> bool:
    """Try to rebuild auto-generated BO4E code"""
    success = False
    with catch_all_exceptions(logging.WARNING, "Could not rebuild auto-generated code"):
        bost_main(
            output=REPO_ROOT / "tmp/bo4e_schemas",
            target_version=version,
            update_refs=True,
            set_default_version=False,
            clear_output=True,
            config_file=REPO_ROOT / "bo4e/bo4e_config.json",
            cache_dir=REPO_ROOT / "tmp/bo4e_cache",
        )
        generate_bo4e_schemas(
            input_directory=REPO_ROOT / "tmp/bo4e_schemas",
            output_directory=REPO_ROOT / "src/ibims/bo4e",
            target_version=version,
            clear_output=True,
            pydantic_v1=False,
        )
        logger.info("Run black and isort on auto-generated code")
        context.invoke(black_main, str(REPO_ROOT / "src/ibims/bo4e"))
        isort_main(str(REPO_ROOT / "src/ibims/bo4e"))
        success = True
    return success


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """
    Check if the current version is up-to-date. If so, exit with exit code 0.
    If not, update the version in the tox.env file and exit with exit code 1.
    """
    os.environ["GIT_PYTHON_TRACE"] = "full"
    with catch_all_exceptions(logging.ERROR, "Could not resolve latest version", exit_code=1):
        latest_version = resolve_latest_version()
    with catch_all_exceptions(logging.ERROR, "Could not resolve current version", exit_code=1):
        current = current_version()

    # if latest_version == current:
    #     logger.info("Version %s is up to date.", current)
    #     return

    with catch_all_exceptions(logging.ERROR, "Could not initialize variables", exit_code=1):
        git_repo = Repo(REPO_ROOT)
        github_repo = Github().get_repo(f"{PR_TARGET_OWNER}/{PR_TARGET_REPO}")
        github_bo4e_repo = Github().get_repo(f"{BO4E_SOURCE_OWNER}/{BO4E_SOURCE_REPO}")
        latest_release = github_bo4e_repo.get_latest_release()
    # If using the script locally with a dirty working directory, stash changes to avoid conflicts
    with catch_all_exceptions(logging.ERROR, "Could not stash changes", exit_code=1):
        git_repo.git.execute(["git", "stash", "push", "--include-untracked"])
    # Checkout new branch to later commit and push changes to remote etc.
    with catch_all_exceptions(logging.ERROR, "Could not new branch", exit_code=1):
        new_branch_name = f"bo4e_bot/bo4e-{latest_version[1:]}"
        new_branch = git_repo.create_head(new_branch_name, logmsg=f"Create branch {new_branch_name}")
        new_branch.checkout()

    # Create some later needed variables before the long rebuilding process. For faster error responses if it fails.
    with catch_all_exceptions(logging.ERROR, "Could not retrieve remote", exit_code=1):
        remotes = git_repo.remotes
        assert len(remotes) == 1, "Expected exactly one remote"
        remote = remotes[0]
        assert remote.exists(), "Remote does not exist"

    # Update BO4E-version in .env file and try to rebuild BO4E
    set_key(DOTENV_FILE, "BO4E_VERSION", latest_version, quote_mode="never")
    succeeded_rebuild = rebuild_bo4e(latest_version, context=ctx)

    # Commit and push changes to remote
    with catch_all_exceptions(logging.ERROR, "Could not push changes to remote", exit_code=1):
        diff = git_repo.index.diff(None)
        git_repo.index.add(diff)
        git_repo.index.commit(f"Update BO4E version to {latest_version}")
        remote.push(f"refs/heads/{new_branch_name}:refs/heads/{new_branch_name}")

    # Create PR with new BO4E version. Even if it couldn't be rebuilt, a new version should be created.
    title = f"Bump BO4E from {current[1:]} to {latest_version[1:]}"
    body = (
        f"{title}.\n"
        f"BO4E rebuild: {'succeeded' if succeeded_rebuild else 'failed'}.\n\n"
        "<details>"
        "<summary>Changelog</summary>"
        f'<p><em>Sourced from <a href="{latest_release.html_url}">'
        "BO4E's changelog</a>.</em></p>"
        "<blockquote>"
        f"<h2>{latest_release.title}</h2>"
        f"{latest_release.body}"
        "</blockquote>"
        "</details>"
    )
    with catch_all_exceptions(logging.ERROR, "Could not create pull request", exit_code=1):
        github_repo.create_pull(
            title=title,
            body=body,
            head=new_branch_name,
            base="main",
        )

    # Pop stash if it was created
    with catch_all_exceptions(logging.ERROR, "Could not pop stash", exit_code=1):
        git_repo.git.stash.pop()


if __name__ == "__main__":
    main()
