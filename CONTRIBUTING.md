# Contibution guide

## Architecture

The SDK is split into two parts: an automatically generated layer of
API bindings and the high-level abstractions built on top. The goal of
this architecture is to reduce the amount of low-level detail stored
in the hand-written code, since this detail is hard to keep in sync
with the API evolution. By automatically generating the bindings
from up-to-date API specs the underlying low-level bindings can be
reasonably expected to be compatible and incompatibilities in the
calls to those bindings can be caught with Pydantic type checking
and linting.

Therefore API compatibility is reduced to code-level detail as much
as possible, with the low-level compatibility being handled by
[OpenAPI Generator](https://openapi-generator.tech/). All code
related to the API bindings is under the `bindings` folder. The code
stored in there should not be touched, modifications should be
carried out by replacing or modifying the OpenAPI specification
files (e.g. `qos-api.json` or `location-api.json`) stored in there
and regenerating the code using `generate-bindings.sh`.

The resulting code in the `bindings` directory is imported as
libraries by the high-level abstractions in the `network_as_code`
module. Note that when adding a new API, you need to add it as
a vendored dependency in `pyproject.toml`.

## Development

### First time setup

Requirements: [python-poetry](https://python-poetry.org/docs/)

1. Clone the repo
2. Install the project
   ```bash
   poetry install
   ```

### Making changes

1. Create a branch
2. Make changes (remember to document your code using docstrings)
3. Write tests and run them locally. Make sure they all pass!
4. Commit and push your branch
5. Submit merge request

If your change involves integrating a new or changed API, you should
include the OpenAPI spec in the `bindings` folder and generate
API bindings from it. Your high-level abstractions should only call
the API through these bindings and you should always expose
functionality to the developers through the high-level abstractions.

The key part of designing and implementing the high-level abstractions
is to consider the third-party developer perspective. Consider if the
terminology and wording in your function names or parameters is
understandable. Consider in what context a particular functionality
should live and what its relationships to other features or concepts
are. Make the functionality discoverable using auto-completion. If
two features function similarly, make sure they have a consistent
appearance to the developer.

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
