# NaC-py - Python SDK for controlling 5G network through code

## Why Network as Code?

So far mobile network configurations from customer's point of view have been fairly immutable. The customer purchases a network connection with a specified download and upload speed for their device and the network supplies a bandwidth as close to those specifications as possible, although congestion or distance to base stations may lead to high variance. The customer's applications are also generally not aware of the network conditions and their ability to react to poor network quality are limited. If the customer wants to modify their network configuration, they must contact the service provider and order a different network subscription. The new network connection will be available typically in a matter of days.

Network as Code is an initiative to create APIs, software libraries and developer portals that make mobile networks configurable by third-party software developers. The aim is to allow application software to be more aware of the mobile network and better leverage its dynamic properties. One of the central ideas is for developers to be able to adjust various network properties on the fly at a seconds' notice to react changing conditions in either the network or the application domain.

You can read more about Network as Code on the [ATG Confluence page](https://confluence.ext.net.nokia.com/display/ATG/ATS+-+Network+as+Code).

This repository contains the Python library for the Network as Code project. It allows Python-based applications to alter the network and query device information such as location data. The library will grow over time to include more functionality as well.

## Getting started

### Installation
Install `network_as_code`  
*Currently available in Nokia's internal [pypi repository](https://pypi.dynamic.nsn-net.net/nac/nacpy)*

```bash
python -m pip install --extra-index-url=https://pypi.dynamic.nsn-net.net/nac/nacpy/+simple/ network_as_code
```

**or**

To include in  `requirements.txt`:
```
--extra-index-url https://pypi.dynamic.nsn-net.net/nac/nacpy/+simple/
network_as_code
```

### Getting access to the APIs

From the developers' point of view, Network as Code consists of two main parts: the language-specific Network as Code SDK and the underlying APIs. The SDK abstracts the APIs, so that developers mostly shouldn't need to deal with the APIs directly. However, the API level also contains the authentication to the Network as Code functionality. To use the SDK, developers need to supply both a valid API access token and a valid device ID for a mobile device on the available 5G environment. Currently Network as Code only works in an internal test network in Chicago.

To gain an API token, you need to register an account on the Apigee developer portal here: https://cns-apigee-test-6559-nacpoc.apigee.io/

More detailed instructions are available here: https://gitlabe2.ext.net.nokia.com/atg/network-as-code/nac-py/-/wikis/home#getting-access-to-the-apis

### Usage

You can now create a Python project and use the Network as Code Python package along with your API key and device ID:

```python
import network_as_code as nac

device = nac.Device(DEVICE_ID, API_TOKEN)

print("API connection established: ", device.check_api_connection())
```

If the program prints "API connection established: True" then you've successfully connected to the Network as Code API through the Python library.

You can also see [app.py](https://gitlabe2.ext.net.nokia.com/atg/network-as-code/nac-py/-/blob/master/app.py) for a demonstrating of a wide range of Network as Code functionalities exposed by the Python library. You can also find documentation for individual classes and methods [on the wiki](https://gitlabe2.ext.net.nokia.com/atg/network-as-code/nac-py/-/wikis/home).

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
