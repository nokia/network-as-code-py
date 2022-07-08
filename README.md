# NaC-py - Python SDK for controlling 5G network through code

This repository contains the Python client for the Network as Code REST API. 
It allows Python-based applications to alter the network profiles and query device information such as location data. 
The library will grow over time to include more functionality as well.

## Why Network as Code?

So far mobile network configurations from customer's point of view have been fairly immutable. 
The customer purchases a network connection with a specified download and upload speed for their device and the network supplies a bandwidth as close to those specifications as possible,
although congestion or distance to base stations may lead to high variance. 
The customer's applications are also generally not aware of the network conditions and their ability to react to poor network quality are limited. 
If the customer wants to modify their network configuration, 
they must contact the service provider and order a different network subscription. 
The new network connection will be available typically in a matter of days.

Network as Code is an initiative to create APIs, 
software libraries and developer portals that make mobile networks configurable by third-party software developers. 
The aim is to allow application software to be more aware of the mobile network and better leverage its dynamic properties. 
One of the central ideas is for developers to be able to adjust various network properties on the fly at a seconds' notice to react changing conditions in either the network or the application domain.

You can read more about Network as Code concept on the [ATG Confluence page](https://confluence.ext.net.nokia.com/display/ATG/ATS+-+Network+as+Code).

## Getting started

> **NOTE:** Below is a quick-start guide. More detailed instructions are available on our [wiki](https://gitlabe2.ext.net.nokia.com/atg/network-as-code/nac-py/-/wikis/home#getting-access-to-the-apis).

### Requirements

* [Sign up](https://cns-apigee-test-6559-nacpoc.apigee.io/) for a Network as Code account
* Create a new [App registration](https://cns-apigee-test-6559-nacpoc.apigee.io/my-apps/new-app). **Enable** the Network as Code API.
* Create a test device (fill in you API key, and come up with an email address, IMSI and MSISDN numbers):  
  Remember the email address you give as it will be used as your device ID.
  ```bash
  curl --request PUT \
  'https://apigee-api-test.nokia-solution.com/nac/v2/subscriber/testuser' \
  --header 'x-testmode: true' \
  --header 'x-apikey: [YOUR_API_KEY]' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{"id":"[SOME EMAIL ADRRESS]","imsi":"[UNIQUE IMSI]","msisdn":"[UNIQUE MSISDN]"}' \
  --compressed

  ```

After these steps you're ready to begin building something awesome with Network as Code!

### Installation

Install the Network as Code package:
```bash
pip install --extra-index-url=https://pypi.dynamic.nsn-net.net/nac/nacpy/+simple/ network_as_code
```
> **NOTE:** The SDK is currently hosted on Nokia's [pypi repository](https://pypi.dynamic.nsn-net.net/nac/nacpy) and requires **VPN** to be properly configured. 

## Examples

We have put some self-explanatory examples in the [examples](./examples) directory, 
but here is a quick example on how to get started. 
Assuming the installation was successful, you can import the Network as Code package like this:

```python
import network_as_code as nac
```

Then, create an instance of **nac.Device**.

The `DEVICE_ID` is the email address you gave during setup.
Meanwhile, the `API_TOKEN` can be found on your [Apps page](https://cns-apigee-test-6559-nacpoc.apigee.io/my-apps) in the API portal.

```python
device = nac.Device(DEVICE_ID, API_TOKEN)
```

Now you can query the API for information and send requests. 
For example, to test that you're able to contact the API, try the following:

```python
print("API connection established: ", device.check_api_connection())
```

If the program prints `API connection established: True`, you've successfully connected to the Network as Code API through the Python library.

In order to start executing other API calls for self-registered devices, you **must** enable test-mode, since self-registered devices
are entirely virtual. You can do so by setting the `TESTMODE` environment variable separately or with the following Python code:

``` python
import os

os.environ["TESTMODE"] = "1"
```

That will cause the SDK to issue requests with a test-mode header to inform the API that the device being queried or altered is a virtual device.

## Documentation

- More in-depth getting-started guide available on the Wiki pages (left sidebar)
- Reference documentation is available [here](https://atg.gitlabe2-pages.ext.net.nokia.com/network-as-code/nac-py/network_as_code/index.html).
