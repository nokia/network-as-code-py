# Contribution guide

## Architecture

The SDK is based on a layered approach of API bindings and the abstractions
built on top of them. The basic idea is that the API bindings only focus on
transformations between the API calls and the higher-level, abstracted
models.

The API bindings live in `network_as_code/api/` and each API "product" has
its own API implementation in its own file. These API bindings are not
exposed as a public interface and developers shouldn't call them directly
from applications.

The abstractions are further split into three categories:
- Namespaces (inside `network_as_code/namespaces`)
- Models (inside `network_as_code/models`)
- Errors (inside `network_as_code/errors`)

### Namespaces

Namespaces are a way to group functions in a particular area together. These
namespaces are imported in `network_as_code/client.py` and exposed as properties
of the client object, allowing them to be accessed like this:

```py
client = NetworkAsCodeClient(...)

client.<namespace>.<method>(...)
```

Namespaces generally call into the API bindings to query or modify Network as Code
resources.

### Models

Models, as the name implies, are representations of resources, events or
equipment. They should be represented as classes with methods for actions
that modify or query information related to a specific instance of the
resource being modeled.

Generally, Namespaces provide functions for producing Model objects, 
such as retrieving one/many instances of a particular resource type.

Models can also call into the API bindings for actions affecting the
individual instance of a resource. Sometimes Models can also provide
functionality which relates to other types of Models if those instances
are related to the Model. An example of this would be the `Device`
model providing methods to create or delete `QoDSession` objects:

```py
device = client.devices.get(...)

session = device.create_qod_session(...)

device.clear_sessions()
```

Models form the main core of the SDK and typically any type of data that
the API deals with has an associated Model in the SDK. The SDK can also
provide its own Models which have no direct equivalent in the API if that
improves the abstractions.

### Errors

Errors are representations of different kinds of failures and exceptions
and are typically mappings to different error codes and messages produced
by the API.

Different Error types are derived from the `NaCError` base class and they
are raised from `httpx` error types. This way we can carry information
from the original error in the API bindings into the `NaCErrors`.

Currently the Error types exposed by the NaC SDK are generic and essentially
just a one-to-one mapping to a particular HTTP error code. However, in the
future these can be extended to cover more situational exceptions as needed.

## Design thinking

The following pillars guide the design and development of the SDKs:

1. User-friendly: minimize assumptions about developer's skill level or familiarity
2. Discoverable: you should provide a path to find functionality via code completion
3. Logically grouped: features should be grouped to models and namespaces logically based on use case similarity
4. Clear: models and functionalities should be clearly named using generally understood terminology - avoid telco-speak
5. Consistent: you should aim to keep conventions consistent between features
6. Prefers one true path: there should be one obvious, correct way to do something - options are concessions
7. API informs, doesn't decide: SDK should match the capabilities of the API, but isn't bound by them

## Development

### First time setup

Requirements: [python-poetry](https://python-poetry.org/docs/)

1. Clone the repo
2. Install the project
   ```bash
   poetry install
   ```

### End-to-end development process

For SDK development, a Test-Driven Development methodology is highly recommended
and at the very least test should be created immediately after a new feature or
a modification of an existing one has been completed. This way mistakes can be
caught earlier and refactoring of the code can be performed with less fear about
introducing compatibility problems with the API.

Tests are split into two categories: unit tests in the `tests` folder and integration
tests in the `integration_tests` folder.

Unit tests use the old definition of "unit", meaning that the intention is not to
tests single functions or classes in isolation, but execute test cases which can
be run independently of external systems and in parallel (no dependency between
test runs). Therefore our unit tests often look like full scenario tests, except
they are run against a mocked API.

Integration tests often look similar to the unit tests, but they are executed against
an actual API instance. From the SDK point of view it doesn't matter whether the
API calls are actually executed against a simulator environment, since the main
aim of the SDK integration tests is to verify that the API bindings are compatible
with the API.

Development usually starts with an OpenAPI specification for a new API feature.
The API implementation may not be ready or deployed yet, so the first part of
development will likely take place against mocks. 

The developer should create new tests in the `tests` folder (should
use existing files, if the API product already has some tests or
create a new file for an entirely new API product).  These mocked
tests use `pytest_httpx` as the mock library. The tests should
construct mock objects to represent different scenarios as accurately
as possible based on the API behavior in the OpenAPI specification.
Then the SDK code should be modified to make these tests pass.

Developers can either write one test at a time and make the test pass
(traditional TDD style) or write a larger number of tests up-front and
make these tests pass in one go. However, unless the developer has a
particular preference, the first option is recommended.

A feature can already be merged when only the unit tests have passed,
but if API has already been deployed then integration tests should be
included in the merge request. Otherwise integration tests should be
provided as an additional MR.

For integration testing more or less the same scenarios should be
considered as with unit tests. However, it's worth noting that
integration tests will run slower than unit tests, so some minor
scenarios may be omitted. In general it is best to be thorough though.
Integration tests __never__ run against mocks, so the use of
`pytest_httpx` is entirely forbidden in integration tests.

A feature which passes all of its unit tests and integration tests
can be considered complete.

### Dealing with API issues, flaky tests, untestable scenarios - xfails and skips

Sometimes the API may introduce bugs which break existing tests or
make it impossible for some new tests to succeed. These should be
reported to the API team for proper correction.

However, there may be situations when a correction cannot be issued
in time and the SDK must release with failing tests. For this,
the [Pytest xfail functionality can be used](https://docs.pytest.org/en/6.2.x/skipping.html).
The SDK configures xfail to be strict, meaning that a successful
xfailed test is a test failure. If an xfailed test starts working
correctly, the xfail should be removed.

Skips should only be used if a particular functionality is not
expected to be delivered or if a particular scenario can never
actually happen. Skips should be used sparingly otherwise or
preferably not at all.

Flaky tests, ones that sometimes work and sometimes don't,
are an indication of a bug and therefore should be corrected.
Tests should always be written in a way that they deterministically
succeed or fail and API behavior should also match this expectation.
Our expectation is that the API team provides a predictable
environment to be tested against and deviations from this
expectation should be considered issues to be fixed.

### Acquiring new OAS specification from API implementation

The API service implementations use FastAPI and are developed at https://gitlabe2.ext.net.nokia.com/nwac/api
It is possible to launch the individual services using `uvicorn` like so:

```bash 
uvicorn --app-dir scripts/ <service-name>:app
```

For example, QoD service can be launched like this:

```bash 
uvicorn --app-dir scripts/ qos:app
```

Navigating into http://localhost:8000/docs should then yield the integrated
FastAPI specification view, which matches that of Swagger. It also has a link
to http://localhost:8000/openapi.json which contains the generated OAS spec.

You can then just download that into any directory you want.

### Branch workflow

1. Create a branch
2. Make changes (remember to document your code using docstrings)
3. Write tests and run them locally. Make sure they all pass!
4. Commit and push your branch
5. Submit merge request

The key part of designing and implementing high-level abstractions
is to consider the third-party developer perspective. Consider if the
terminology and wording in your function names or parameters is
understandable. Consider in what context a particular functionality
should live and what its relationships to other features or concepts
are. Make the functionality discoverable using auto-completion. If
two features function similarly, make sure they have a consistent
appearance to the developer.

## Testing and test coverage

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
