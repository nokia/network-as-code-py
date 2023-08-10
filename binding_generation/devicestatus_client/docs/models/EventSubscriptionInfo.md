# devicestatus_client.model.event_subscription_info.EventSubscriptionInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**eventSubscriptionId** | str,  | str,  | The event subscription identifier | 
**webhook** | [**Webhook**](Webhook.md) | [**Webhook**](Webhook.md) |  | 
**[subscriptionDetail](#subscriptionDetail)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Event subscription details | 
**subscriptionExpireTime** | str,  | str,  | The subscription expiration time in date-time format | [optional] 
**maxNumberOfReports** | decimal.Decimal, int,  | decimal.Decimal,  | Number of notifications until the subscription is available | [optional] 
**startsAt** | str,  | str,  | date time when subscription started | [optional] 
**expiresAt** | str,  | str,  | date time when subscription will expire or expired | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subscriptionDetail

Event subscription details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Event subscription details | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EventSubscriptionDetail](EventSubscriptionDetail.md) | [**EventSubscriptionDetail**](EventSubscriptionDetail.md) | [**EventSubscriptionDetail**](EventSubscriptionDetail.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
