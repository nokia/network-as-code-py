# Contibution guide

## Development

### First time setup

Requirements: [python-poetry](https://python-poetry.org/docs/)

1. Clone the repo
1. Install the project
   ```bash
   poetry install
   ```

### Making changes

1. Create a branch
1. Make changes (remember to document your code using docstrings)
1. Write tests and run them locally. Make sure they all pass!
1. Commit and push your branch
1. Submit merge request

## Testing

Using [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/config.html) for reporting line coverage,
which is a wrapper for the [`coverage`](https://coverage.readthedocs.io/en/6.2/index.html) library.  
Read their respective documentation to learn more about the possible configuration options.

### Example commands

**Quick check:**

```bash
poetry run pytest --cov=network_as_code
```

**HTML report:**

```bash
poetry run pytest --cov-report html --cov=network_as_code
```

**HTML report with branch checks:**

```bash
poetry run pytest -cov-branch --cov-report html --cov=network_as_code
```