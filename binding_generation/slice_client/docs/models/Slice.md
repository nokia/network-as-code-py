# slice_client.model.slice.Slice

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**areaOfService** | [**AreaOfService**](AreaOfService.md) | [**AreaOfService**](AreaOfService.md) |  | 
**notificationUrl** | str,  | str,  | Contact attached to the order to send back information regarding this order. | 
**networkIdentifier** | [**NetworkIdentifier**](NetworkIdentifier.md) | [**NetworkIdentifier**](NetworkIdentifier.md) |  | 
**sliceInfo** | [**SliceInfo**](SliceInfo.md) | [**SliceInfo**](SliceInfo.md) |  | 
**name** | str,  | str,  | Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as \&quot;Concert-2029-Big-Arena\&quot;. | [optional] 
**notificationAuthToken** | str,  | str,  | Authorization token for notification sending. | [optional] 
**maxDataConnections** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of data connection sessions in the slice. | [optional] 
**maxDevices** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of devices using the slice. | [optional] 
**sliceDownlinkThroughput** | [**Throughput**](Throughput.md) | [**Throughput**](Throughput.md) |  | [optional] 
**sliceUplinkThroughput** | [**Throughput**](Throughput.md) | [**Throughput**](Throughput.md) |  | [optional] 
**deviceDownlinkThroughput** | [**Throughput**](Throughput.md) | [**Throughput**](Throughput.md) |  | [optional] 
**deviceUplinkThroughput** | [**Throughput**](Throughput.md) | [**Throughput**](Throughput.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

