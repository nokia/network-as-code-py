# NaC-py - Python SDK for controlling 5G network through code

This repository contains the Python library for the Network as Code project. It allows Python-based applications to alter the network and query device information such as location data. The library will grow over time to include more functionality as well.

## Why Network as Code?

So far mobile network configurations from customer's point of view have been fairly immutable. The customer purchases a network connection with a specified download and upload speed for their device and the network supplies a bandwidth as close to those specifications as possible, although congestion or distance to base stations may lead to high variance. The customer's applications are also generally not aware of the network conditions and their ability to react to poor network quality are limited. If the customer wants to modify their network configuration, they must contact the service provider and order a different network subscription. The new network connection will be available typically in a matter of days.

Network as Code is an initiative to create APIs, software libraries and developer portals that make mobile networks configurable by third-party software developers. The aim is to allow application software to be more aware of the mobile network and better leverage its dynamic properties. One of the central ideas is for developers to be able to adjust various network properties on the fly at a seconds' notice to react changing conditions in either the network or the application domain.

You can read more about Network as Code on the [ATG Confluence page](https://confluence.ext.net.nokia.com/display/ATG/ATS+-+Network+as+Code).

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

You can also see [the examples folder](https://gitlabe2.ext.net.nokia.com/atg/network-as-code/nac-py/-/tree/master/examples) for a demonstration of a wide range of Network as Code functionalities exposed by the Python library. You can also find documentation for individual classes and methods [on our pdoc page](https://atg.gitlabe2-pages.ext.net.nokia.com/network-as-code/nac-py/network_as_code/index.html).
