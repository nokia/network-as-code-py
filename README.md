# NaC-py - Python SDK for controlling 5G network through code

## Installation

```bash
pip install network_as_code
```

## Development

Requirements: [python-poetry](https://python-poetry.org/docs/)

1. Clone the repo
1. Install the project
   ```bash
   poetry install
   ```
1. Make changes
1. Write tests
1. Submit merge request

## Documentation

> **TODO:** Add link to docs, etc.

## Testing

Using [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/config.html) for reporting line coverage,
which is a wrapper for the [`coverage`](https://coverage.readthedocs.io/en/6.2/index.html) library.  
Read their respective documentation to learn more about the possible configuration options.

### Examples

Quick check:

```bash
poetry run pytest --cov=network_as_code
```

HTML report:

```bash
poetry run pytest --cov-report html --cov=network_as_code
```

HTML report with branch checks:

```bash
poetry run pytest -cov-branch --cov-report html --cov=network_as_code
```
