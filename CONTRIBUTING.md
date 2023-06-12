# Contribution guide

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

Since the SDK is split into code-generated and handwritten parts,
depending on what you are working on the workflow may be different.

This section aims to clarify how to perform typical changes in
the SDK. It also clarifies which steps can be performed in which
order in order to maximize development efficiency.

In general, the SDK is always downstream of specification and
often downstream of API implementation. This means that the
process usually goes like this:

```
+---------------------+
|                     |
|  High-level spec    |
|                     |
+---------+-----------+
          |
          |
          |
+---------+-----------+
|                     |
|  API implementation |
|                     |
+---------+-----------+
          |
          |
          |
+---------+-----------+
|                     |
|   OAS generation    |
|                     |
+---------------------+
          |
          |
          |
+---------+-----------+
|                     |
|   Code generation   |
|                     |
+---------+-----------+
          |
          |
          |
+---------+-----------+
|                     |
|    Abstraction      |
|                     |
+---------------------+
```

Essentially, features are outlined in a high-level specification,
which is used to inform the API implementation. The OAS spec is
then derived from the API implementation and code generation used
to integrate the API into the SDK. Abstractions are then built
on top of the generated code to expose a nicer interface.

However, an alternative workflow can be followed for more
developer efficiency without being blocked by API implementation
as much:

```
+---------------------+
|                     |
|  High-level spec    +--------------------
|                     |                   |
+---------+-----------+                   |
          |                               |
          |                               |
          |                               |
+---------+-----------+       +-----------+------------+
|                     |       |                        |
|  API implementation |       |   Abstraction w/ stubs |
|                     |       |                        |
+---------+-----------+       +-----------+------------+
          |                               |
          |                               |
          |                               |
+---------+-----------+                   |
|                     |                   |
|   OAS generation    |                   |
|                     |                   |
+---------------------+                   |
          |                               |
          |                               |
          |                               |
+---------+-----------+      +------------+-------------+
|                     |      |                          |
|   Code generation   +------+ Connect API+abstractions |
|                     |      |                          |
+---------+-----------+      +--------------------------+
```

This approach allows you to create the high-level interfaces concurrent
to the actual API implementation, assuming that the high-level spec
is sufficiently clear about how the abstractions may look like.

The abstractions in this case would need to be coded against mocks and
stubs pending the actual implementation. However, this should only
leave the final integration of generated code as the last necessary
step towards integrating a change.

#### Integrating new / changed APIs

The workflow of integrating new or changed APIs mostly requires work
in the code generation and OAS specification massaging, the high-level
abstraction work is typically very light.

Assuming process workflow 1 (no high-level abstractions up-front),
the process for this consists of these steps:

1. Acquire new OAS specification file containing the change
2. Massage the OAS specification to include security headers and necessary changes
3. Run code generation to create a client library
4. Include generated client library as a vendored dependency of the project
5. Import client library under  `network_as_code/api/client.py` and initialize it inside `APIClient`
6. Create high-level abstractions, hook up calls from models to the `APIClient`

##### Acquiring new OAS specification

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

##### Massaging the OAS specification

By default, the OAS specification lacks information about security keys
and may require further changes.

One example of necessary changes arises when a field sometimes returns
null values. By default FastAPI doesn't reflect this change in the spec,
so you may have to add this information yourself. To do this, just add
`"nullable": true` to the specification file in the required schema
field:

```json
"country": {
    "title": "Country",
    "type": "string",
    "nullable": true
}
```

For authentication options, you should include the following under `components`:

```json
    "securitySchemes": {
      "RapidApiKey": {
        "type": "apiKey",
        "in": "header",
        "name": "X-RapidAPI-Key"
      }
    },
```

And add the following field to the specification:

```json
  "security": [
    {
       "RapidApiKey": []
    }
  ]
```

##### Code generation using OpenAPI-Generator

**NOTE**: OpenAPI-Generator requires Java. It is recommended to use OpenJDK 11, newer or older versions may not work correctly.

A script for code generation is included in `binding_generation/generate-binding.sh`.
To generate new API bindings, copy OAS specs into `binding_generation` and modify
the script and then run it. To regenerate bindings for changed APIs, replace the existing
OAS specification file and rerun the script.

##### Vendoring generated code as dependencies

In order for the project to use the generated code, it must be included as a vendored
dependency of the project.

To do this, open `pyproject.toml` and check the `packages` section:

```toml
packages = [
    { include = "network_as_code" },
    { include = "qos_client", from = "binding_generation"},
    { include = "location_client", from = "binding_generation"}
]
```

You must modify this to include the generated client library from `binding_generation`.
Otherwise the package may work locally but it won't install correctly on other systems.

After that, add the client library as a dependency:

```toml
[tool.poetry.dependencies]
...
location_client = {path = "./binding_generation/location_client", develop = true}
```

This ensures that the library can be imported.

##### Importing generated code in APIClient

The `network_as_code/api/client.py` file contains the linkages to generated code.

First import the API from the generated client library:

```python
import location_client.api_client as location_api_client

from location_client.apis.tags import location_api
```

Then inside the `__init__()` method include a base_url parameter for the API
and initialize the client library as a member of the `APIClient` object:

```python
class APIClient:
    # ...
    def __init__(
        self,
        token: str,
        # ...
        location_base_url: str = "https://location-verification.p-eu.rapidapi.com",
        **kwargs,
    ):
        # ...
        location_config = location_api_client.Configuration(
            host=location_base_url,
            api_key={
                "RapidApiKey": token
            }
        )

        self._location_client = location_api_client.ApiClient(
            location_config,
            header_name="X-RapidAPI-Host",
            header_value="location-verification.nokia-dev.rapidapi.com"
        )

        self.location = location_api.LocationApi(self._location_client)
```

##### Create high-level abstractions

Abstractions should be created in the `network_as_code` folder, split
into `models`, `errors` and `namespaces`. 

Models represent concepts and group functionality that is specific to
a specific instance of data returned from the API, or an abstract concept
around the APIs, such as a specific Device.

Errors provide exception types that are context-specific and informative
to the third-party developers. High-level abstractions should aim to use
high-level exception types rather than relying on HTTPExceptions if
possible.

Namespaces are used to group functionality together and to provide the
initial path from the `NetworkAsCodeClient` to the functionality. Their
main purpose is to make functionality discoverable using code completion
frameworks.

### Branch workflow

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
