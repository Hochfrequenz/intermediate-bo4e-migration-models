# Intermediate BO4E M**I**gration Models (ibims)

![Unittests status badge](https://github.com/Hochfrequenz/bo4e-migration-model/workflows/Unittests/badge.svg)
![Coverage status badge](https://github.com/Hochfrequenz/bo4e-migration-model/workflows/Coverage/badge.svg)
![Linting status badge](https://github.com/Hochfrequenz/bo4e-migration-model/workflows/Linting/badge.svg)
![Formatting status badge](https://github.com/Hochfrequenz/bo4e-migration-model/workflows/Formatting/badge.svg)

A data model for migrating data from one system to another.
The package name is "ibims".

### Installation

It's also [available on pypi](https://pypi.org/project/ibims/).
```bash
pip install ibims
```

### Documentation
There is a (very early stage) documentation of this repository on [readthedocs](https://intermediate-bo4e-migration-models.readthedocs.io/de/latest/api/ibims.html).

## How to use this Repository on Your Machine

This repository uses [uv](https://docs.astral.sh/uv/) for dependency management and tooling.
Install uv, then set up the development environment with:
```bash
uv sync --group dev
uv run pre-commit install
```
Run the tooling via the corresponding dependency groups, e.g.:
```bash
uv run --group tests python -m pytest
uv run --group linting ruff check .
uv run --group linting ruff format --check .
uv run --group type_check mypy --show-error-codes src/ibims
```
The BO4E models in `src/ibims/bo4e` are generated from the configuration in `bo4e/`. Regenerate them with:
```bash
source bo4e/tox.env  # sets BO4E_VERSION
uv run --group generate_bo4e bost -o "tmp/bo4e_schemas" -t "$BO4E_VERSION" -c "bo4e/bo4e_config.json" --clear-output --cache-dir "tmp/bo4e_cache"
uv run --group generate_bo4e bo4e-generator -i "tmp/bo4e_schemas" -o "src/ibims/bo4e" --clear-output -t "$BO4E_VERSION"
```

For general guidance, see our [Python template repository](https://github.com/Hochfrequenz/python_template_repository#how-to-use-this-repository-on-your-machine).

## Contribute

You are very welcome to contribute to this template repository by opening a pull request against the main branch.
