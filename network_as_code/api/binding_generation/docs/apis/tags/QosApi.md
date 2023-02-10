<a name="__pageTop"></a>
# openapi_client.apis.tags.qos_api.QosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_subscribe_sessions_post**](#send_subscribe_sessions_post) | **post** /sessions | Create QoS service

# **send_subscribe_sessions_post**
<a name="send_subscribe_sessions_post"></a>
> AsSessionWithQoSSubscription send_subscribe_sessions_post(qo_s_resource)

Create QoS service

Create device communication bandwidth (QoS) service.

### Example

```python
import openapi_client
from openapi_client.apis.tags import qos_api
from openapi_client.model.qo_s_resource import QoSResource
from openapi_client.model.as_session_with_qo_s_subscription import AsSessionWithQoSSubscription
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qos_api.QosApi(api_client)

    # example passing only required values which don't have defaults set
    body = QoSResource(
        qos="qos_example",
        id="id_example",
        ip="ip_example",
        ports="ports_example",
        app_ip="app_ip_example",
        app_ports="app_ports_example",
    )
    try:
        # Create QoS service
        api_response = api_instance.send_subscribe_sessions_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QosApi->send_subscribe_sessions_post: %s\n" % e)
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
[**QoSResource**](../../models/QoSResource.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#send_subscribe_sessions_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#send_subscribe_sessions_post.ApiResponseFor422) | Validation Error

#### send_subscribe_sessions_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsSessionWithQoSSubscription**](../../models/AsSessionWithQoSSubscription.md) |  | 


#### send_subscribe_sessions_post.ApiResponseFor422
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

