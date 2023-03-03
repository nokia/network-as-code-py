<a name="__pageTop"></a>
# openapi_client.apis.tags.qos_api.QosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_qos_sessions_post**](#create_qos_sessions_post) | **post** /sessions | Create QoS service
[**delete_qos_sessions_resource_id_delete**](#delete_qos_sessions_resource_id_delete) | **delete** /sessions/{resource_id} | Delete Qos
[**get_qos_sessions_resource_id_get**](#get_qos_sessions_resource_id_get) | **get** /sessions/{resource_id} | Return QoS settings

# **create_qos_sessions_post**
<a name="create_qos_sessions_post"></a>
> SessionInfo create_qos_sessions_post(create_session)

Create QoS service

Create device communication bandwidth (QoS) service.

### Example

* Api Key Authentication (RapidApiKey):
```python
import openapi_client
from openapi_client.apis.tags import qos_api
from openapi_client.model.create_session import CreateSession
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.session_info import SessionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qos_api.QosApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateSession(
        qos="qos_example",
        id="id_example",
        ip="ip_example",
        ports=PortsSpec(
            ranges=[
                PortsSpecRangesInner(
                    _from=1.0,
                    to=1.0,
                )
            ],
            ports=[
                1.0
            ],
        ),
        app_ip="app_ip_example",
        app_ports=PortsSpec(),
    )
    try:
        # Create QoS service
        api_response = api_instance.create_qos_sessions_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QosApi->create_qos_sessions_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateSession**](../../models/CreateSession.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_qos_sessions_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#create_qos_sessions_post.ApiResponseFor422) | Validation Error

#### create_qos_sessions_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SessionInfo**](../../models/SessionInfo.md) |  | 


#### create_qos_sessions_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[RapidApiKey](../../../README.md#RapidApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_qos_sessions_resource_id_delete**
<a name="delete_qos_sessions_resource_id_delete"></a>
> delete_qos_sessions_resource_id_delete(resource_id)

Delete Qos

### Example

* Api Key Authentication (RapidApiKey):
```python
import openapi_client
from openapi_client.apis.tags import qos_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qos_api.QosApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource_id': "resource_id_example",
    }
    try:
        # Delete Qos
        api_response = api_instance.delete_qos_sessions_resource_id_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QosApi->delete_qos_sessions_resource_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource_id | ResourceIdSchema | | 

# ResourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_qos_sessions_resource_id_delete.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#delete_qos_sessions_resource_id_delete.ApiResponseFor422) | Validation Error

#### delete_qos_sessions_resource_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_qos_sessions_resource_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[RapidApiKey](../../../README.md#RapidApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_qos_sessions_resource_id_get**
<a name="get_qos_sessions_resource_id_get"></a>
> SessionInfo get_qos_sessions_resource_id_get(resource_id)

Return QoS settings

Return device communication bandwidth (QoS) settings.

### Example

* Api Key Authentication (RapidApiKey):
```python
import openapi_client
from openapi_client.apis.tags import qos_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.session_info import SessionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qos_api.QosApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource_id': "resource_id_example",
    }
    try:
        # Return QoS settings
        api_response = api_instance.get_qos_sessions_resource_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QosApi->get_qos_sessions_resource_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resource_id | ResourceIdSchema | | 

# ResourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_qos_sessions_resource_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_qos_sessions_resource_id_get.ApiResponseFor422) | Validation Error

#### get_qos_sessions_resource_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SessionInfo**](../../models/SessionInfo.md) |  | 


#### get_qos_sessions_resource_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[RapidApiKey](../../../README.md#RapidApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

