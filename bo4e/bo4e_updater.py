"""
This script checks if the current BO4E version is up-to-date.
"""
import sys

import click
import requests
from dotenv import dotenv_values, set_key

OWNER = "Hochfrequenz"
REPO = "BO4E-Schemas"
TIMEOUT = 10  # in seconds
DOTENV_FILE = "bo4e/tox.env"


def resolve_latest_version() -> str:
    """
    Resolve the latest BO4E version from the github api.
    """
    response = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest", timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()["tag_name"]


def current_version() -> str:
    """
    Query the current version from the tox.env file
    """
    config = dotenv_values(DOTENV_FILE)
    assert config["BO4E_VERSION"] is not None
    return config["BO4E_VERSION"]


@click.command()
def main():
    """
    Check if the current version is up-to-date. If so, exit with exit code 0.
    If not, update the version in the tox.env file and exit with exit code 1.
    """
    latest_version = resolve_latest_version()
    current = current_version()
    if latest_version == current:
        print(f"Version {current} is up to date.")
        return

    # Update BO4E:
    set_key(DOTENV_FILE, "BO4E_VERSION", latest_version)
    sys.exit(1)


if __name__ == "__main__":
    main()
