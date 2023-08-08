<a id="__pageTop"></a>
# slice_client.apis.tags.default_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_slices**](#get_all_slices) | **get** /slices | Returns All Slices

# **get_all_slices**
<a id="get_all_slices"></a>
> [SliceData] get_all_slices()

Returns All Slices

Returns All created Network Slices

### Example

* Api Key Authentication (RapidApiKey):
```python
import slice_client
from slice_client.apis.tags import default_api
from slice_client.model.slice_data import SliceData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slice_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: RapidApiKey
configuration.api_key['RapidApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['RapidApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with slice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns All Slices
        api_response = api_instance.get_all_slices()
        pprint(api_response)
    except slice_client.ApiException as e:
        print("Exception when calling DefaultApi->get_all_slices: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_slices.ApiResponseFor200) | Successful Response

#### get_all_slices.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SliceData**]({{complexTypePrefix}}SliceData.md) | [**SliceData**]({{complexTypePrefix}}SliceData.md) | [**SliceData**]({{complexTypePrefix}}SliceData.md) |  | 

### Authorization

[RapidApiKey](../../../README.md#RapidApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

