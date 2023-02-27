# openapi_client.model.as_session_with_qo_s_subscription.AsSessionWithQoSSubscription

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qosReference** | str,  | str,  | Reference of the requested QoS level | 
**[flowInfo](#flowInfo)** | list, tuple,  | tuple,  | Flow informations that might be affected by the given QoS operation | 
**self** | str,  | str,  | Resource URL of the subscription | [optional] 
**supportedFeatures** | str,  | str,  | Resource URL of the subscription | [optional] 
**ueIpv4Addr** | str,  | str,  | IPV4 address of the device | [optional] 
**ueIpv6Addr** | str,  | str,  | IPV4 address of the device | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flowInfo

Flow informations that might be affected by the given QoS operation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Flow informations that might be affected by the given QoS operation | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FlowInfo**](FlowInfo.md) | [**FlowInfo**](FlowInfo.md) | [**FlowInfo**](FlowInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

