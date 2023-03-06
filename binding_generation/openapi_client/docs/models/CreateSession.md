# openapi_client.model.create_session.CreateSession

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**appIp** | str,  | str,  | IP address of the application | 
**qos** | str,  | str,  | Name of the requested QoS | 
**ip** | str,  | str,  | IP address of the device | 
**id** | str,  | str,  | Identifier of the device | 
**ports** | [**PortsSpec**](PortsSpec.md) | [**PortsSpec**](PortsSpec.md) |  | [optional] 
**appPorts** | [**PortsSpec**](PortsSpec.md) | [**PortsSpec**](PortsSpec.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

