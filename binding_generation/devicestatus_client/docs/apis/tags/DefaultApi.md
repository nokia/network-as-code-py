<a name="__pageTop"></a>
# devicestatus_client.apis.tags.default_api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connectivity_subscription**](#create_connectivity_subscription) | **post** /connectivity | Create subscription for device connectivity status
[**create_event_subscription**](#create_event_subscription) | **post** /event-subscriptions | Create subscription for device status events
[**delete_connectivity**](#delete_connectivity) | **delete** /connectivity/{id} | Delete Connectivity Handler
[**delete_event_subscription**](#delete_event_subscription) | **delete** /event-subscriptions/{id} | Delete Event Subscription Handler
[**get_connectivity**](#get_connectivity) | **get** /connectivity/{id} | Get device connectivity status
[**get_event_subscription**](#get_event_subscription) | **get** /event-subscriptions/{id} | Retrieve a device status event subscription for a device
[**update_connectivity**](#update_connectivity) | **put** /connectivity/{id} | Update device connectivity status

# **create_connectivity_subscription**
<a name="create_connectivity_subscription"></a>
> ConnectivityData create_connectivity_subscription(connectivity_subscription)

Create subscription for device connectivity status

Create subscription for device connectivity status.

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.connectivity_data import ConnectivityData
from devicestatus_client.model.http_validation_error import HTTPValidationError
from devicestatus_client.model.connectivity_subscription import ConnectivitySubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConnectivitySubscription(
        device=None,
        id="id_example",
        max_num_of_reports=1.0,
        notification_url="notification_url_example",
        notification_auth_token="notification_auth_token_example",
    )
    try:
        # Create subscription for device connectivity status
        api_response = api_instance.create_connectivity_subscription(
            body=body,
        )
        pprint(api_response)
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->create_connectivity_subscription: %s\n" % e)
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
[**ConnectivitySubscription**](../../models/ConnectivitySubscription.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_connectivity_subscription.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#create_connectivity_subscription.ApiResponseFor422) | Validation Error

#### create_connectivity_subscription.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectivityData**](../../models/ConnectivityData.md) |  | 


#### create_connectivity_subscription.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_event_subscription**
<a name="create_event_subscription"></a>
> EventSubscriptionInfo create_event_subscription(create_event_subscription)

Create subscription for device status events

Create subscriptions for device status events.

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.event_subscription_info import EventSubscriptionInfo
from devicestatus_client.model.create_event_subscription import CreateEventSubscription
from devicestatus_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateEventSubscription(
        subscription_detail=None,
        subscription_expire_time="subscription_expire_time_example",
        max_number_of_reports=1,
        webhook=Webhook(
            notification_url="notification_url_example",
            notification_auth_token="notification_auth_token_example",
        ),
    )
    try:
        # Create subscription for device status events
        api_response = api_instance.create_event_subscription(
            body=body,
        )
        pprint(api_response)
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->create_event_subscription: %s\n" % e)
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
[**CreateEventSubscription**](../../models/CreateEventSubscription.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_event_subscription.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#create_event_subscription.ApiResponseFor422) | Validation Error

#### create_event_subscription.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EventSubscriptionInfo**](../../models/EventSubscriptionInfo.md) |  | 


#### create_event_subscription.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_connectivity**
<a name="delete_connectivity"></a>
> delete_connectivity(id)

Delete Connectivity Handler

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete Connectivity Handler
        api_response = api_instance.delete_connectivity(
            path_params=path_params,
        )
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_connectivity: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_connectivity.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#delete_connectivity.ApiResponseFor422) | Validation Error

#### delete_connectivity.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_connectivity.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_event_subscription**
<a name="delete_event_subscription"></a>
> delete_event_subscription(id)

Delete Event Subscription Handler

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete Event Subscription Handler
        api_response = api_instance.delete_event_subscription(
            path_params=path_params,
        )
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_event_subscription: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_event_subscription.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#delete_event_subscription.ApiResponseFor422) | Validation Error

#### delete_event_subscription.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_event_subscription.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_connectivity**
<a name="get_connectivity"></a>
> ConnectivityData get_connectivity(id)

Get device connectivity status

Retrieve device connectivity status data

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.connectivity_data import ConnectivityData
from devicestatus_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get device connectivity status
        api_response = api_instance.get_connectivity(
            path_params=path_params,
        )
        pprint(api_response)
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->get_connectivity: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_connectivity.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_connectivity.ApiResponseFor422) | Validation Error

#### get_connectivity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectivityData**](../../models/ConnectivityData.md) |  | 


#### get_connectivity.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_event_subscription**
<a name="get_event_subscription"></a>
> EventSubscriptionInfo get_event_subscription(id)

Retrieve a device status event subscription for a device

retrieve event subscription information for a given subscription

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.event_subscription_info import EventSubscriptionInfo
from devicestatus_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Retrieve a device status event subscription for a device
        api_response = api_instance.get_event_subscription(
            path_params=path_params,
        )
        pprint(api_response)
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->get_event_subscription: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_event_subscription.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_event_subscription.ApiResponseFor422) | Validation Error

#### get_event_subscription.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EventSubscriptionInfo**](../../models/EventSubscriptionInfo.md) |  | 


#### get_event_subscription.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_connectivity**
<a name="update_connectivity"></a>
> ConnectivityData update_connectivity(idconnectivity_subscription)

Update device connectivity status

Update device connectivity status data

### Example

```python
import devicestatus_client
from devicestatus_client.apis.tags import default_api
from devicestatus_client.model.connectivity_data import ConnectivityData
from devicestatus_client.model.http_validation_error import HTTPValidationError
from devicestatus_client.model.connectivity_subscription import ConnectivitySubscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devicestatus_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with devicestatus_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = ConnectivitySubscription(
        device=None,
        id="id_example",
        max_num_of_reports=1.0,
        notification_url="notification_url_example",
        notification_auth_token="notification_auth_token_example",
    )
    try:
        # Update device connectivity status
        api_response = api_instance.update_connectivity(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except devicestatus_client.ApiException as e:
        print("Exception when calling DefaultApi->update_connectivity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectivitySubscription**](../../models/ConnectivitySubscription.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_connectivity.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_connectivity.ApiResponseFor422) | Validation Error

#### update_connectivity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectivityData**](../../models/ConnectivityData.md) |  | 


#### update_connectivity.ApiResponseFor422
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

