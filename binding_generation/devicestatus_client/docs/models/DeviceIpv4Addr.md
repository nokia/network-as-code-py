# devicestatus_client.model.device_ipv4_addr.DeviceIpv4Addr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**publicAddress** | str,  | str,  | Public IPv4 address of the device. Either of the device or the NAT the device is behind. | [optional] 
**privateAddress** | str,  | str,  | Private IPv4 address of the device, if it is behind a NAT. | [optional] 
**publicPort** | decimal.Decimal, int,  | decimal.Decimal,  | Public port used by the device. Port is necessary, as private address ranges overlap, and public port is used to extend the range for CGNAT. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

