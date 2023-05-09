# qos_client.model.session_info.SessionInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qosProfile** | str,  | str,  | Name of the QoS profile. | 
**qosStatus** | str,  | str,  | Status of the QoS resource. REQUESTED, AVAILABLE or UNAVAILABLE | 
**id** | str,  | str,  | ID of the created resource. | 
**startedAt** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Timestamp of session start in seconds since unix epoch | [optional] 
**expiresAt** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Timestamp of session expiration if the session was not deleted, in seconds since unix epoch | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
