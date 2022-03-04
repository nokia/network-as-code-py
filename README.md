# NaC-py - Python SDK for controlling 5G network through code

## Installation

```bash
python -m pip install nac-py --extra-index-url https://pypi.dynamic.nsn-net.net/<group>
```

## Documentation

Documentation can be found in the [project wiki](https://gitlabe2.ext.net.nokia.com/atgi/network-as-code/nac-py/-/wikis/home).

## Development

Requirements: [python-poetry](https://python-poetry.org/docs/)

1. Clone the repo
1. Install the project
   ```bash
   poetry install
   ```
1. Make changes
1. Write and run tests
1. Write and update docstrings
1. Submit merge request
1. After the merge request has been merged:
   1. Generate Markdown docs for each file (class) you made changes to
      ```bash
      poetry run pydoc-markdown -m network_as_code.<class> --render-toc > docs.md
      ```
   1. Edit/create the respective pages under _Reference_, in the [project wiki](https://gitlabe2.ext.net.nokia.com/atgi/network-as-code/nac-py/-/wikis/home).

## Testing

Using [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/config.html) for reporting line coverage,
which is a wrapper for the [`coverage`](https://coverage.readthedocs.io/en/6.2/index.html) library.  
Read their respective documentation to learn more about the possible configuration options.

### Examples

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
