# Reference
## Slice
<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">get_device_attachments</a>() -> typing.List[GetDeviceAttachmentsSliceResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the given device attach resources associated with the owner.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.get_device_attachments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">attach_device</a>(...) -> AttachDeviceSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach device to a specific network slice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.slice import AttachDeviceSliceRequestDevice, AttachDeviceSliceRequestCustomer, AttachDeviceSliceRequestTrafficCategories, AttachDeviceSliceRequestTrafficCategoriesApps, AttachDeviceSliceRequestWebhook

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.attach_device(
    device=AttachDeviceSliceRequestDevice(
        phone_number="+99999991000",
        imsi=99999991000,
    ),
    customer=AttachDeviceSliceRequestCustomer(
        name="DefaultAttachOperationCustomer",
        description="I Am Default Who Order The Device Attach Operation",
        address="Dummy Customer Address",
        contact="My Contact Should Be Here",
    ),
    slice_id="slice-773",
    mobile_services=[
        "Voice",
        "Voicemail",
        "5G-Data"
    ],
    traffic_categories=AttachDeviceSliceRequestTrafficCategories(
        apps=AttachDeviceSliceRequestTrafficCategoriesApps(
            os="09078034-07db-4b13-a970-ab80235f7369",
            apps=[
                "Daedalus"
            ],
        ),
    ),
    webhook=AttachDeviceSliceRequestWebhook(
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a396071",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `AttachDeviceSliceRequestDevice` 
    
</dd>
</dl>

<dl>
<dd>

**slice_id:** `str` — Slice resource identifier, simple name or UUID.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[AttachDeviceSliceRequestCustomer]` — Customer who orders the device attach operations.
    
</dd>
</dl>

<dl>
<dd>

**mobile_services:** `typing.Optional[typing.List[str]]` — List of services allowed for the device.
    
</dd>
</dl>

<dl>
<dd>

**traffic_categories:** `typing.Optional[AttachDeviceSliceRequestTrafficCategories]` — Denotes the operating system id and the applications' identifiers
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[AttachDeviceSliceRequestWebhook]` — Callback settings for the requester application.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">activate</a>(...) -> ActivateSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activate a network slice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.activate(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">get_device_attachment</a>(...) -> GetDeviceAttachmentSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the given device attach resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.get_device_attachment(
    resource_id="resource_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">delete_device_attachment</a>(...) -> DeleteDeviceAttachmentSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach device from a specific slice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.delete_device_attachment(
    resource_id="resource_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">deactivate</a>(...) -> DeactivateSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate a network slice. The slice state must be active to be able to perform this operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.deactivate(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">list_slices</a>() -> typing.List[ListSlicesSliceResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns All created Network Slices
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.list_slices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">create_slice</a>(...) -> CreateSliceSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a network slice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.slice import CreateSliceSliceRequestNetworkIdentifier, CreateSliceSliceRequestSliceInfo, CreateSliceSliceRequestSliceUplinkThroughput, CreateSliceSliceRequestDeviceUplinkThroughput

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.create_slice(
    notification_url="https://example.com/notify",
    notification_auth_token="6207f4c159esfnjsf6280c0e8417090d91710b8c9369f21d9b616ebe809d28c5dc4b1428447fa5d83988b516595253bae24e2a9eb22f43523f2ab1997dd7",
    network_identifier=CreateSliceSliceRequestNetworkIdentifier(
        mcc="236",
        mnc="30",
    ),
    slice_info=CreateSliceSliceRequestSliceInfo(
        service_type=1,
        differentiator="0003E8",
    ),
    max_data_connections=42312,
    max_devices=33,
    slice_uplink_throughput=CreateSliceSliceRequestSliceUplinkThroughput(
        guaranteed=15,
        maximum=999999,
    ),
    device_uplink_throughput=CreateSliceSliceRequestDeviceUplinkThroughput(
        guaranteed=10,
        maximum=20,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_url:** `str` — Contact attached to the order to send back information regarding this order.
    
</dd>
</dl>

<dl>
<dd>

**network_identifier:** `CreateSliceSliceRequestNetworkIdentifier` 
    
</dd>
</dl>

<dl>
<dd>

**slice_info:** `CreateSliceSliceRequestSliceInfo` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event.
    
</dd>
</dl>

<dl>
<dd>

**notification_auth_token:** `typing.Optional[str]` — Authorization token for notification sending.
    
</dd>
</dl>

<dl>
<dd>

**area_of_service:** `typing.Optional[CreateSliceSliceRequestAreaOfService]` — Specifies the area where the slice can be used
    
</dd>
</dl>

<dl>
<dd>

**max_data_connections:** `typing.Optional[int]` — Maximum number of data connection sessions in the slice.
    
</dd>
</dl>

<dl>
<dd>

**max_devices:** `typing.Optional[int]` — Maximum number of devices using the slice.
    
</dd>
</dl>

<dl>
<dd>

**delay_tolerance:** `typing.Optional[str]` — Delaytolerance attribute, True/False or SUPPORTED/NOT SUPPORTED
    
</dd>
</dl>

<dl>
<dd>

**service_priority:** `typing.Optional[int]` — ServicePriority attribute
    
</dd>
</dl>

<dl>
<dd>

**slice_downlink_throughput:** `typing.Optional[CreateSliceSliceRequestSliceDownlinkThroughput]` — Data rate parameters (max/guaranteed) supported by the network slice for all devices together in downlink
    
</dd>
</dl>

<dl>
<dd>

**slice_uplink_throughput:** `typing.Optional[CreateSliceSliceRequestSliceUplinkThroughput]` — Data rate parameters (max/guaranteed) supported by the network slice for all devices together in uplink
    
</dd>
</dl>

<dl>
<dd>

**device_downlink_throughput:** `typing.Optional[CreateSliceSliceRequestDeviceDownlinkThroughput]` — Data rate parameters (max/guaranteed) supported by the network slice per device in downlink
    
</dd>
</dl>

<dl>
<dd>

**device_uplink_throughput:** `typing.Optional[CreateSliceSliceRequestDeviceUplinkThroughput]` — Data rate parameters (max/guaranteed) supported by the network slice per device in uplink
    
</dd>
</dl>

<dl>
<dd>

**isolation_level:** `typing.Optional[CreateSliceSliceRequestIsolationLevel]` — Parameter describing the isolation type
    
</dd>
</dl>

<dl>
<dd>

**qos:** `typing.Optional[str]` — QoS Identifier
    
</dd>
</dl>

<dl>
<dd>

**udm5qi:** `typing.Optional[str]` — 5G QoS Identifier
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[CreateSliceSliceRequestCustomer]` — Customer created the slice
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">subscriber_operation</a>(...) -> SubscriberOperationSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create subscriber in a given slice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.slice import SubscriberOperationSliceRequestDevice, SubscriberOperationSliceRequestCustomer, SubscriberOperationSliceRequestTrafficCategories, SubscriberOperationSliceRequestTrafficCategoriesApps, SubscriberOperationSliceRequestWebhook

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.subscriber_operation(
    operation="create",
    device=SubscriberOperationSliceRequestDevice(
        phone_number="+99999991000",
        imsi=99999991000,
    ),
    customer=SubscriberOperationSliceRequestCustomer(
        name="DefaultAttachOperationCustomer",
        description="I Am Default Who Order The Device Attach Operation",
        address="Dummy Customer Address",
        contact="My Contact Should Be Here",
    ),
    slice_id="slice-773",
    mobile_services=[
        "Voice",
        "Voicemail",
        "5G-Data"
    ],
    traffic_categories=SubscriberOperationSliceRequestTrafficCategories(
        apps=SubscriberOperationSliceRequestTrafficCategoriesApps(
            os="09078034-07db-4b13-a970-ab80235f7369",
            apps=[
                "Daedalus"
            ],
        ),
    ),
    webhook=SubscriberOperationSliceRequestWebhook(
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a396071",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation:** `SubscriberOperationSliceRequestOperation` 
    
</dd>
</dl>

<dl>
<dd>

**device:** `SubscriberOperationSliceRequestDevice` 
    
</dd>
</dl>

<dl>
<dd>

**slice_id:** `str` — Slice resource identifier, simple name or UUID.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[SubscriberOperationSliceRequestCustomer]` — Customer who orders the device attach operations.
    
</dd>
</dl>

<dl>
<dd>

**mobile_services:** `typing.Optional[typing.List[str]]` — List of services allowed for the device.
    
</dd>
</dl>

<dl>
<dd>

**traffic_categories:** `typing.Optional[SubscriberOperationSliceRequestTrafficCategories]` — Denotes the operating system id and the applications' identifiers
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[SubscriberOperationSliceRequestWebhook]` — Callback settings for the requester application.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">get_slice</a>(...) -> GetSliceSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get network slice data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.get_slice(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slice.<a href="src/networkAsCode/slice/client.py">delete_slice</a>(...) -> DeleteSliceSliceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete network slice. The slice state must not be active to perform this operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.slice.delete_slice(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Well Known Metadata
<details><summary><code>client.well_known_metadata.<a href="src/networkAsCode/well_known_metadata/client.py">get_openid_configuration</a>() -> GetOpenidConfigurationWellKnownMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.well_known_metadata.get_openid_configuration()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.well_known_metadata.<a href="src/networkAsCode/well_known_metadata/client.py">get_oauth_authorization_server</a>() -> GetOauthAuthorizationServerWellKnownMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.well_known_metadata.get_oauth_authorization_server()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.well_known_metadata.<a href="src/networkAsCode/well_known_metadata/client.py">get_security_txt</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.well_known_metadata.get_security_txt()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DeviceStatus
<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">get_subscription</a>(...) -> GetSubscriptionDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

retrieve event subscription information for a given subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.get_subscription(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create subscription operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">delete_subscription</a>(...) -> typing.Optional[DeleteSubscriptionDeviceStatusResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

delete a  given event subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.delete_subscription(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">check_connectivity</a>(...) -> CheckConnectivityDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current connectivity status information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import CheckConnectivityDeviceStatusRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.check_connectivity(
    device=CheckConnectivityDeviceStatusRequestDevice(
        phone_number="+99999991000",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `CheckConnectivityDeviceStatusRequestDevice` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">retrieve_roaming_status</a>(...) -> RetrieveRoamingStatusDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current roaming status and the country information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import RetrieveRoamingStatusDeviceStatusRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.retrieve_roaming_status(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    device=RetrieveRoamingStatusDeviceStatusRequestDevice(
        phone_number="+99999991000",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[RetrieveRoamingStatusDeviceStatusRequestDevice]` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">get_roaming_subscription</a>(...) -> GetRoamingSubscriptionDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

retrieve device roaming status subscription information for a given subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.get_roaming_subscription(
    subscription_id="subscriptionId",
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">delete_roaming_subscription</a>(...) -> typing.Optional[DeleteRoamingSubscriptionDeviceStatusResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a given device-roaming-status subscription by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.delete_roaming_subscription(
    subscription_id="subscriptionId",
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">get_reachability_subscription</a>(...) -> GetReachabilitySubscriptionDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a given subscription by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.get_reachability_subscription(
    subscription_id="subscriptionId",
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">delete_reachability_subscription</a>(...) -> typing.Optional[DeleteReachabilitySubscriptionDeviceStatusResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a given subscription by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.delete_reachability_subscription(
    subscription_id="subscriptionId",
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">retrieve_reachability_status</a>(...) -> RetrieveReachabilityStatusDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current reachability status information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import RetrieveReachabilityStatusDeviceStatusRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.retrieve_reachability_status(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    device=RetrieveReachabilityStatusDeviceStatusRequestDevice(
        phone_number="+99999991000",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[RetrieveReachabilityStatusDeviceStatusRequestDevice]` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">list_subscriptions</a>() -> typing.List[ListSubscriptionsDeviceStatusResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of device status event subscription(s)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.list_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">create_subscription</a>(...) -> CreateSubscriptionDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a device status event subscription for a device
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import CreateSubscriptionDeviceStatusRequestSubscriptionDetail, CreateSubscriptionDeviceStatusRequestSubscriptionDetailDevice, CreateSubscriptionDeviceStatusRequestWebhook
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.create_subscription(
    subscription_detail=CreateSubscriptionDeviceStatusRequestSubscriptionDetail(
        device=CreateSubscriptionDeviceStatusRequestSubscriptionDetailDevice(
            phone_number="+36719991000",
        ),
        type="org.camaraproject.device-status.v0.roaming-status",
    ),
    subscription_expire_time=datetime.datetime.fromisoformat("2026-01-17T13:18:23+00:00"),
    webhook=CreateSubscriptionDeviceStatusRequestWebhook(
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a3960714",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_detail:** `CreateSubscriptionDeviceStatusRequestSubscriptionDetail` — The detail of the requested event subscription
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `CreateSubscriptionDeviceStatusRequestWebhook` — Webhook information for event channel
    
</dd>
</dl>

<dl>
<dd>

**subscription_expire_time:** `typing.Optional[datetime.datetime]` — The subscription expiration time in date-time format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">list_roaming_subscriptions</a>(...) -> typing.List[ListRoamingSubscriptionsDeviceStatusResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of device roaming status event subscription(s)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.list_roaming_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">create_roaming_subscription</a>(...) -> CreateRoamingSubscriptionDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a device roaming status event subscription for a device
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import CreateRoamingSubscriptionDeviceStatusRequestConfig, CreateRoamingSubscriptionDeviceStatusRequestConfigSubscriptionDetail, CreateRoamingSubscriptionDeviceStatusRequestConfigSubscriptionDetailDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.create_roaming_subscription(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    protocol="HTTP",
    sink="https://endpoint.example.com/sink",
    types=[
        "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-status"
    ],
    config=CreateRoamingSubscriptionDeviceStatusRequestConfig(
        subscription_detail=CreateRoamingSubscriptionDeviceStatusRequestConfigSubscriptionDetail(
            device=CreateRoamingSubscriptionDeviceStatusRequestConfigSubscriptionDetailDevice(
                phone_number="+99999991000",
            ),
        ),
        subscription_max_events=5,
        initial_event=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `CreateRoamingSubscriptionDeviceStatusRequestProtocol` — Identifier of a delivery protocol. Only HTTP is allowed for now
    
</dd>
</dl>

<dl>
<dd>

**sink:** `str` — The address to which events shall be delivered using the selected protocol.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.List[CreateRoamingSubscriptionDeviceStatusRequestTypesItem]` 

Camara Event types eligible to be delivered by this subscription.
Note: for the current Commonalities version (v0.5) only one event type per subscription is allowed, yet in the following releases use of array of event types SHALL be specified without changing this definition.
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateRoamingSubscriptionDeviceStatusRequestConfig` 

Implementation-specific configuration parameters needed by the subscription manager for acquiring events.
In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`
Specific event type attributes must be defined in `subscriptionDetail`
Note: if a request is performed for several event type, all subscribed event will use same `config` parameters.
    
</dd>
</dl>

<dl>
<dd>

**sink_credential:** `typing.Optional[CreateRoamingSubscriptionDeviceStatusRequestSinkCredential]` — A sink credential provides authentication or authorization information necessary to enable delivery of events to a target.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">check_roaming</a>(...) -> CheckRoamingDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current roaming status and the country information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import CheckRoamingDeviceStatusRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.check_roaming(
    device=CheckRoamingDeviceStatusRequestDevice(
        phone_number="+99999991000",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `CheckRoamingDeviceStatusRequestDevice` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">list_reachability_subscriptions</a>(...) -> typing.List[ListReachabilitySubscriptionsDeviceStatusResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of device reachability status event subscription(s)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.list_reachability_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_status.<a href="src/networkAsCode/device_status/client.py">create_reachability_subscription</a>(...) -> CreateReachabilitySubscriptionDeviceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a device reachability status event subscription for a device
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.device_status import CreateReachabilitySubscriptionDeviceStatusRequestConfig, CreateReachabilitySubscriptionDeviceStatusRequestConfigSubscriptionDetail, CreateReachabilitySubscriptionDeviceStatusRequestConfigSubscriptionDetailDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_status.create_reachability_subscription(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    protocol="HTTP",
    sink="https://endpoint.example.com/sink",
    types=[
        "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
    ],
    config=CreateReachabilitySubscriptionDeviceStatusRequestConfig(
        subscription_detail=CreateReachabilitySubscriptionDeviceStatusRequestConfigSubscriptionDetail(
            device=CreateReachabilitySubscriptionDeviceStatusRequestConfigSubscriptionDetailDevice(
                phone_number="+99999991000",
            ),
        ),
        subscription_max_events=5,
        initial_event=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `CreateReachabilitySubscriptionDeviceStatusRequestProtocol` — Identifier of a delivery protocol. Only HTTP is allowed for now
    
</dd>
</dl>

<dl>
<dd>

**sink:** `str` — The address to which events shall be delivered using the selected protocol.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.List[CreateReachabilitySubscriptionDeviceStatusRequestTypesItem]` 

Camara Event types eligible to be delivered by this subscription.
Note: For the current Commonalities API design guidelines, only one event type per subscription is allowed, yet in the following releases use of array of event types SHALL be specified without changing this definition.
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateReachabilitySubscriptionDeviceStatusRequestConfig` 

Implementation-specific configuration parameters needed by the subscription manager for acquiring events.
In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`
Specific event type attributes must be defined in `subscriptionDetail`
Note: if a request is performed for several event type, all subscribed event will use same `config` parameters.
    
</dd>
</dl>

<dl>
<dd>

**sink_credential:** `typing.Optional[CreateReachabilitySubscriptionDeviceStatusRequestSinkCredential]` — A sink credential provides authentication or authorization information necessary to enable delivery of events to a target.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConsentInfo
<details><summary><code>client.consent_info.<a href="src/networkAsCode/consent_info/client.py">retrieve</a>(...) -> RetrieveConsentInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a request to retrieve the validity status of the API Consumer data processing for a given User, scope(s) and Purpose.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.consent_info.retrieve(
    phone_number="+99999991000",
    scopes=[
        "location-verification:verify"
    ],
    purpose="dpv:FraudPreventionAndDetection",
    request_capture_url=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scopes:** `typing.List[str]` — List of requested scopes. The scope is a string that represents the access rights that the API Consumer is requesting from the User.
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `str` — The reason for which personal data will be processed by the API Consumer. CAMARA defines a standard set of Purposes which can be used by API Consumers to specify the reason for their intended personal data processing. CAMARA uses the [W3C Data Privacy Vocabulary](https://w3c.github.io/dpv/2.0/dpv/) (DPV) to represent these purposes e.g. `dpv:FraudPreventionAndDetection` or `dpv:RequestedServiceProvision`.
    
</dd>
</dl>

<dl>
<dd>

**request_capture_url:** `bool` 

A boolean flag indicating whether the API Consumer requests API Provider to return a Consent capture URL.
* `true` - If set to `true` the API will include a `captureUrl` in the response body if applicable.
* `false` - The API will omit the Consent capture URL from the response.
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[typing.Any]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NumberRecycling
<details><summary><code>client.number_recycling.<a href="src/networkAsCode/number_recycling/client.py">check</a>(...) -> CheckNumberRecyclingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check whether the subscriber of the phone number has changed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.number_recycling.check(
    phone_number="+99999991000",
    specified_date=datetime.date.fromisoformat("2024-10-31"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**specified_date:** `datetime.date` — Specified date to check whether there has been a change in the subscriber associated with the specific phone number, in RFC 3339 calendar date format (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[typing.Any]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NumberVerification
<details><summary><code>client.number_verification.<a href="src/networkAsCode/number_verification/client.py">verify</a>(...) -> VerifyNumberVerificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies if the specified phone number (either in plain text or hashed format) matches the one that the user is currently using. Only one of the plain or hashed formats must be provided.
- The number verification will be done for the user that has authenticated via mobile network
- It returns true/false depending on if the hashed phone number received as input matches the authenticated user's `device phone number` associated to the access token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.number_verification.verify(
    phone_number="+99999991000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**state:** `typing.Optional[str]` — Application state
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Authorization code received from the CSP
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**hashed_phone_number:** `typing.Optional[str]` — Hashed phone number. SHA-256 (in hexadecimal representation) of the mobile phone number in **E.164 format (starting with country code)**. Prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.number_verification.<a href="src/networkAsCode/number_verification/client.py">get_device_phone_number</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.number_verification.get_device_phone_number()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CongestionInsights
<details><summary><code>client.congestion_insights.<a href="src/networkAsCode/congestion_insights/client.py">list_subscriptions</a>() -> typing.List[ListSubscriptionsCongestionInsightsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get congestion subscriptions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.congestion_insights.list_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.congestion_insights.<a href="src/networkAsCode/congestion_insights/client.py">create_subscription</a>(...) -> CreateSubscriptionCongestionInsightsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create device congestion subscription. Notifies if congestion is high, medium, low or none.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.congestion_insights import CreateSubscriptionCongestionInsightsRequestDevice, CreateSubscriptionCongestionInsightsRequestWebhook
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.congestion_insights.create_subscription(
    device=CreateSubscriptionCongestionInsightsRequestDevice(
        phone_number="+36719991000",
    ),
    webhook=CreateSubscriptionCongestionInsightsRequestWebhook(
        notification_url="http://example.com/notify",
        notification_auth_token="c8974e592f9fh683d4a3960714",
    ),
    subscription_expire_time=datetime.datetime.fromisoformat("2045-04-12T09:09:33+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `CreateSubscriptionCongestionInsightsRequestDevice` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `CreateSubscriptionCongestionInsightsRequestWebhook` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_expire_time:** `datetime.datetime` — Time when the subscription expires.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.congestion_insights.<a href="src/networkAsCode/congestion_insights/client.py">get_subscription</a>(...) -> GetSubscriptionCongestionInsightsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get congestion subscription data of the given device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.congestion_insights.get_subscription(
    resource_id="resource_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.congestion_insights.<a href="src/networkAsCode/congestion_insights/client.py">delete_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unsubscribe from congestion event of the given device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.congestion_insights.delete_subscription(
    resource_id="resource_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.congestion_insights.<a href="src/networkAsCode/congestion_insights/client.py">query</a>(...) -> typing.List[QueryCongestionInsightsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch historical or predicted congestion level of a device for a given period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.congestion_insights import QueryCongestionInsightsRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.congestion_insights.query(
    device=QueryCongestionInsightsRequestDevice(
        phone_number="+99999991000",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `QueryCongestionInsightsRequestDevice` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Start of the period queried. If not set, 15 minutes before end. If neither start or end is set, then the upcoming 15 minutes are predicted.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — End of the period queried. If not set, 15 minutes after start.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SimSwap
<details><summary><code>client.sim_swap.<a href="src/networkAsCode/sim_swap/client.py">check</a>(...) -> CheckSimSwapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if SIM swap has been performed during a past period
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.sim_swap.check(
    phone_number="+99999991000",
    max_age=240,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Period in hours to be checked for SIM swap.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sim_swap.<a href="src/networkAsCode/sim_swap/client.py">retrieve_date</a>(...) -> RetrieveDateSimSwapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get timestamp of last SIM swap event for a mobile user account provided with phone number.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.sim_swap.retrieve_date(
    phone_number="+99999991000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Kyc
<details><summary><code>client.kyc.<a href="src/networkAsCode/kyc/client.py">verify_age</a>(...) -> VerifyAgeKycResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify that the age of the subscriber associated with a phone number is equal to or greater than the specified age threshold value.

As it is possible that the person holding the contract and the end-user of the subscription may not be the same, the endpoint also admits a list of optional properties to be included in the request to improve the identification. The response may optionally include the `identityMatchScore` property with a value that indicates how certain it is that the information returned relates to the person that the API Client is requesting. To increase the reliability of the information returned, the API Provider may include in the response the `verifiedStatus` property, indicating whether the identity information in its possession has been verified against an identification document legally accepted as an age verification document.

If the API Client indicates request properties `includeContentLock` or `includeParentalControl` with value `true` and the API Provider implements this functionality, then the response will also include `contentLock` and `parentalControl` properties to indicate if the subscription has any kind of content filtering enabled. On the other hand, if the request properties are not included or the API Client specifies value `false`, then the response properties will not be returned. If the API Provider doesn't implement this functionality, request properties will be ignored and response properties won't be returned in any case.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.kyc.verify_age(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    age_threshold=18,
    phone_number="+99999991000",
    id_document="66666666q",
    name="Federica Sanchez Arjona",
    given_name="Federica",
    family_name="Sanchez Arjona",
    middle_names="Sanchez",
    family_name_at_birth="YYYY",
    birthdate=datetime.date.fromisoformat("1978-08-22"),
    email="federicaSanchez.Arjona@example.com",
    include_content_lock=True,
    include_parental_control=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**age_threshold:** `int` — The age to be verified. The indicated range is a global definition of maximum and minimum values allowed to be requested. It is important to note that this range might be more restrictive in some implementations due to local regulations of a country i.e. A country does not allow to request for an age under 18. This limitation must be informed during the onboarding process.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**id_document:** `typing.Optional[str]` — Id number associated to the official identity document in the country. It may contain alphanumeric characters.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Complete name of the customer, usually composed of first/given name and last/family/sur- name in a country.  Depending on the country, the order of first/give name and last/family/sur- name varies, and middle name could be included.  It can use givenName, middleNames, familyName and/or familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` — First/given name or compound first/given name of the customer.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — Last name, family name, or surname of the customer.
    
</dd>
</dl>

<dl>
<dd>

**middle_names:** `typing.Optional[str]` — Middle name/s of the customer.
    
</dd>
</dl>

<dl>
<dd>

**family_name_at_birth:** `typing.Optional[str]` — Last/family/sur- name at birth of the customer.
    
</dd>
</dl>

<dl>
<dd>

**birthdate:** `typing.Optional[datetime.date]` — The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the customer in the RFC specified format (local-part@domain).
    
</dd>
</dl>

<dl>
<dd>

**include_content_lock:** `typing.Optional[bool]` — If this parameter is included in the request with value `true`, the response property `contentLock` will be returned. If it is not included or its value is `false`, the response property will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**include_parental_control:** `typing.Optional[bool]` — If this parameter is included in the request with value `true`, the response property `parentalControl` will be returned. If it is not included or its value is `false`, the response property will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/networkAsCode/kyc/client.py">check_tenure</a>(...) -> CheckTenureKycResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies a specified length of tenure, based on a provided date, for a network subscriber to establish a level of trust for the network subscription identifier.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.kyc.check_tenure(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    phone_number="+99999991000",
    tenure_date=datetime.date.fromisoformat("2023-07-03"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**tenure_date:** `datetime.date` — The date, in RFC 3339 / ISO 8601 compliant format "YYYY-MM-DD", from which continuous tenure of the identified network subscriber is required to be confirmed
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/networkAsCode/kyc/client.py">match</a>(...) -> MatchKycResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify matching of a number of attributes related to a customer identity against the verified data bound to their phone number in the Operator systems. Regardless of whether the `phoneNumber` is explicitly stated in the request body, at least one of the other fields must be provided, otherwise a `HTTP 400 - KNOW_YOUR_CUSTOMER.INVALID_PARAM_COMBINATION` error will be returned.

In order to proceed with the match check, some Operators may have the requirement to perform an additional level of validation based on the `idDocument` property. This means that, in those cases, the `idDocument` is required and the provided value needs to match the one stored in the Operator system associated with the indicated `phoneNumber`. This validation will be done before proceeding with the match check of the rest of the properties. The following two rules apply only in the cases where the Operator have the requirement to validate the `idDocument`:
- If no `idDocument` is provided, then a `HTTP 403 - KNOW_YOUR_CUSTOMER.ID_DOCUMENT_REQUIRED` error will be returned.
- If the provided `idDocument` does not match the one stored in the Operator systems, then a `HTTP 403 - KNOW_YOUR_CUSTOMER.ID_DOCUMENT_MISMATCH` error will be returned.

The API will return the result of the matching process for each requested attribute. This means that the response will **only** contain the attributes for which validation has been requested. Possible values are:





  - **true**: the attribute provided matches with the one in the Operator systems.
  - **false**: the attribute provided does not match with the one in the Operator systems.
  - **not_available**: the attribute is not available to validate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.kyc.match(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    phone_number="+99999991000",
    id_document="66666666q",
    name="Federica Sanchez Arjona",
    given_name="Federica",
    family_name="Sanchez Arjona",
    name_kana_hankaku="federica",
    name_kana_zenkaku="Ｆｅｄｅｒｉｃａ",
    middle_names="Sanchez",
    family_name_at_birth="YYYY",
    address="Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
    street_name="Nicolas Salmeron",
    street_number="4",
    postal_code="1028460",
    region="Tokyo",
    locality="ZZZZ",
    country="JP",
    house_number_extension="VVVV",
    birthdate=datetime.date.fromisoformat("1978-08-22"),
    email="abc@example.com",
    gender="OTHER",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**id_document:** `typing.Optional[str]` — Id number associated to the official identity document in the country. It may contain alphanumeric characters.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Complete name of the customer, usually composed of first/given name and last/family/sur- name in a country.  Depending on the country, the order of first/give name and last/family/sur- name varies, and middle name could be included.  It can use givenName, middleNames, familyName and/or familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` — First/given name or compound first/given name of the customer.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — Last name, family name, or surname of the customer.
    
</dd>
</dl>

<dl>
<dd>

**name_kana_hankaku:** `typing.Optional[str]` — Complete name of the customer in Hankaku-Kana format (reading of name) for Japan.
    
</dd>
</dl>

<dl>
<dd>

**name_kana_zenkaku:** `typing.Optional[str]` — Complete name of the customer in Zenkaku-Kana format (reading of name) for Japan.
    
</dd>
</dl>

<dl>
<dd>

**middle_names:** `typing.Optional[str]` — Middle name/s of the customer.
    
</dd>
</dl>

<dl>
<dd>

**family_name_at_birth:** `typing.Optional[str]` — Last/family/sur- name at birth of the customer.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[str]` — Complete address of the customer.  For some countries, it is built following the usual concatenation of parameters in a country, but for other countries, this is not the case.  For some countries, it can use streetName, streetNumber and/or houseNumberExtension. For example, in ESP, streetName+streetNumber; in NLD, it can be streetName+streetNumber or streetName+streetNumber+houseNumberExtension.
    
</dd>
</dl>

<dl>
<dd>

**street_name:** `typing.Optional[str]` — Name of the street of the customer's address. It should not include the type of the street.
    
</dd>
</dl>

<dl>
<dd>

**street_number:** `typing.Optional[str]` — The street number of the customer's address.  Number identifying a specific property on the 'streetName'.
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — Zip code or postal code
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Region/prefecture of the customer's address
    
</dd>
</dl>

<dl>
<dd>

**locality:** `typing.Optional[str]` — Locality of the customer's address
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Country of the customer's address. Format ISO 3166-1 alpha-2
    
</dd>
</dl>

<dl>
<dd>

**house_number_extension:** `typing.Optional[str]` — Specific identifier of the house needed depending on the property type. For example, number of apartment in an apartment building.
    
</dd>
</dl>

<dl>
<dd>

**birthdate:** `typing.Optional[datetime.date]` — The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the customer in the RFC specified format (local-part@domain).
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[MatchKycRequestGender]` — Gender of the customer (Male/Female/Other).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/networkAsCode/kyc/client.py">fill_in</a>(...) -> FillInKycResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.kyc.fill_in(
    phone_number="+99999991000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Optional[typing.Any]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Qod
<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">get_session_v1</a>(...) -> GetSessionV1QodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Querying for QoS session resource information details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.get_session_v_1(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID that was obtained from the createSession operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">delete_session_v1</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Release resources related to QoS session

If the notification callback is provided and the `qosStatus` of the session was `AVAILABLE` the client will receive in addition to the response a `QOS_STATUS_CHANGED` event with
- `qosStatus` as `UNAVAILABLE` and
- `statusInfo` as `DELETE_REQUESTED`
There will be no notification event if the `qosStatus` was already `UNAVAILABLE`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.delete_session_v_1(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID that was obtained from the createSession operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">list_sessions_v1</a>() -> typing.List[ListSessionsV1QodResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return device communication Quality-on-Demand settings for your devices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.list_sessions_v_1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">create_session_v1</a>(...) -> CreateSessionV1QodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create QoS Session to manage latency/throughput priorities

If the qosStatus in the API response is "AVAILABLE" and a notification callback is provided the API consumer will receive in addition to the response a
`QOS_STATUS_CHANGED` event notification with `qosStatus` as `AVAILABLE`.

If the `qosStatus` in the API response is `REQUESTED`, the client will receive either
- a `QOS_STATUS_CHANGED` event notification with `qosStatus` as `AVAILABLE` after the network notifies that it has created the requested session, or
- a `QOS_STATUS_CHANGED` event notification with `qosStatus` as `UNAVAILABLE` and `statusInfo` as `NETWORK_TERMINATED` after the network notifies that it has failed to provide the requested session.

A `QOS_STATUS_CHANGED` event notification with `qosStatus` as `UNAVAILABLE` will also be send if the network terminates the session before the requested duration expired

NOTE: in case of a `QOS_STATUS_CHANGED` event with `qosStatus` as `UNAVAILABLE` and `statusInfo` as `NETWORK_TERMINATED` the resources of the QoS session
are not directly released, but will get deleted automatically at earliest 360 seconds after the event.
This behavior allows clients which are not receiving notification events but are polling to get the session information with
the `qosStatus` `UNAVAILABLE` (the `statusInfo` parameter is not included in the current version but will be adding to `SessionInfo` in an upcoming release). Before a client can attempt to create a new QoD session
for the same device and flow period they must release the session resources with an explicit `delete` operation if not yet automatically deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.qod import CreateSessionV1QodRequestDevice, CreateSessionV1QodRequestApplicationServer

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.create_session_v_1(
    device=CreateSessionV1QodRequestDevice(
        phone_number="+99999991001",
        ipv_4_address={"publicAddress": "233.252.0.2", "privateAddress": "192.0.2.25", "publicPort": 80},
    ),
    application_server=CreateSessionV1QodRequestApplicationServer(
        ipv_4_address="8.8.8.8",
    ),
    qos_profile="DOWNLINK_M_UPLINK_L",
    duration=60,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_server:** `CreateSessionV1QodRequestApplicationServer` 

A server hosting backend applications to deliver some business logic to clients.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
    
</dd>
</dl>

<dl>
<dd>

**qos_profile:** `str` 

A unique name for identifying a specific QoS profile.
This may follow different formats depending on the service providers implementation.
Some options addresses:





  - A UUID style string
  - Support for predefined profiles QOS_S, QOS_M, QOS_L, and QOS_E
  - A searchable descriptive name
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[CreateSessionV1QodRequestDevice]` 

End-user equipment able to connect to a network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
    
</dd>
</dl>

<dl>
<dd>

**device_ports:** `typing.Optional[CreateSessionV1QodRequestDevicePorts]` — The ports used locally by the device for flows to which the requested QoS profile should apply. If omitted, then the qosProfile will apply to all flows between the device and the specified application server address and ports
    
</dd>
</dl>

<dl>
<dd>

**application_server_ports:** `typing.Optional[CreateSessionV1QodRequestApplicationServerPorts]` — A list of single ports or port ranges on the application server
    
</dd>
</dl>

<dl>
<dd>

**sink:** `typing.Optional[str]` — The address to which events about all status changes of the session (e.g. session termination) shall be delivered using the selected protocol.
    
</dd>
</dl>

<dl>
<dd>

**sink_credential:** `typing.Optional[CreateSessionV1QodRequestSinkCredential]` — A sink credential provides authentication or authorization information necessary to enable delivery of events to a target.
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` 

Session duration in seconds. Maximal value of 24 hours is used if not set.
After session is expired the, client will receive a `QOS_STATUS_CHANGED` event with
- `qosStatus` as `UNAVAILABLE`, and,
- `statusInfo` as `DURATION_EXPIRED`.
See notification callback.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">list_sessions</a>() -> typing.List[ListSessionsQodResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return device communication Quality-on-Demand settings for your devices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.list_sessions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">create_session</a>(...) -> CreateSessionQodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create QoS Session to manage latency/throughput priorities

If the qosStatus in the API response is "AVAILABLE" and a notification callback is provided the client will receive in addition to the response a
`QOS_STATUS_CHANGED` event notification with `qosStatus` as `AVAILABLE`.

If the `qosStatus` in the API response is `REQUESTED`, the client will receive either
- a `QOS_STATUS_CHANGED` event notification with `qosStatus` as `AVAILABLE` after the network notifies that it has created the requested session, or
- a `QOS_STATUS_CHANGED` event notification with `qosStatus` as `UNAVAILABLE` and `statusInfo` as `NETWORK_TERMINATED` after the network notifies that it has failed to provide the requested session.

A `QOS_STATUS_CHANGED` event notification with `qosStatus` as `UNAVAILABLE` will also be send if the network terminates the session before the requested duration expired

NOTE: in case of a `QOS_STATUS_CHANGED` event with `qosStatus` as `UNAVAILABLE` and `statusInfo` as `NETWORK_TERMINATED` the resources of the QoS session
are not directly released, but will get deleted automatically at earliest 360 seconds after the event.
This behavior allows clients which are not receiving notification events but are polling to get the session information with
the `qosStatus` `UNAVAILABLE` (the `statusInfo` parameter is not included in the current version but will be adding to `SessionInfo` in an upcoming release). Before a client can attempt to create a new QoD session
for the same device and flow period they must release the session resources with an explicit `delete` operation if not yet automatically deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.qod import CreateSessionQodRequestDevice, CreateSessionQodRequestApplicationServer

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.create_session(
    device=CreateSessionQodRequestDevice(
        phone_number="+99999991001",
        ipv_4_address={"publicAddress": "233.252.0.2", "privateAddress": "192.0.2.25", "publicPort": 80},
    ),
    application_server=CreateSessionQodRequestApplicationServer(
        ipv_4_address="8.8.8.8",
    ),
    qos_profile="DOWNLINK_M_UPLINK_L",
    duration=60,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `CreateSessionQodRequestDevice` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
    
</dd>
</dl>

<dl>
<dd>

**application_server:** `CreateSessionQodRequestApplicationServer` 

A server hosting backend applications to deliver some business logic to clients.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
    
</dd>
</dl>

<dl>
<dd>

**qos_profile:** `str` 

A unique name for identifying a specific QoS profile.
This may follow different formats depending on the service providers implementation.
Some options addresses:





  - A UUID style string
  - Support for predefined profiles QOS_S, QOS_M, QOS_L, and QOS_E
  - A searchable descriptive name
    
</dd>
</dl>

<dl>
<dd>

**device_ports:** `typing.Optional[CreateSessionQodRequestDevicePorts]` — The ports used locally by the device for flows to which the requested QoS profile should apply. If omitted, then the qosProfile will apply to all flows between the device and the specified application server address and ports
    
</dd>
</dl>

<dl>
<dd>

**application_server_ports:** `typing.Optional[CreateSessionQodRequestApplicationServerPorts]` — A list of single ports or port ranges on the application server
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[CreateSessionQodRequestWebhook]` 
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[int]` 

Session duration in seconds. Maximal value of 24 hours is used if not set.
After session is expired the, client will receive a `QOS_STATUS_CHANGED` event with
- `qosStatus` as `UNAVAILABLE`, and,
- `statusInfo` as `DURATION_EXPIRED`.
See notification callback.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">retrieve_sessions_v1</a>(...) -> typing.List[RetrieveSessionsV1QodResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all QoD sessions related to the specified device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.qod import RetrieveSessionsV1QodRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.retrieve_sessions_v_1(
    device=RetrieveSessionsV1QodRequestDevice(
        phone_number="+99999991001",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `RetrieveSessionsV1QodRequestDevice` 

End-user equipment able to connect to a network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">extend_session_v1</a>(...) -> ExtendSessionV1QodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extend the overall duration of an active QoS session. If this operation is executed successfully, the new duration of the target session will be the original duration plus the additionally requested duration.
The new remaining duration of the QoS session shall not exceed the maximum remaining duration limit (currently fixed at 86,400 seconds) where the remaining duration is calculated as the difference between the `expiresAt` and current time when the request to extend the session duration is received. If this maximum limit would be exceeded, the overall duration shall be set such that the remaining duration is equal to this limit.
An example: A QoD session was originally created with duration 80,000 seconds. 10,000 seconds later, the developer requested to extend the session by 20,000 seconds.
- Original duration: 80,000 seconds
- Elapsed time: 10,000 seconds
- Remaining duration: 70,000 seconds
- New remaining duration: 86,400 seconds (the maximum allowed)
- New overall session duration: 96,400 seconds
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.extend_session_v_1(
    session_id="sessionId",
    requested_additional_duration=60,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID that was obtained from the createSession operation
    
</dd>
</dl>

<dl>
<dd>

**requested_additional_duration:** `int` — Additional duration in seconds to be extended.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">extend_session</a>(...) -> ExtendSessionQodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extend the overall duration of an active QoS session. If this operation is executed successfully, the new duration of the target session will be the original duration plus the additionally requested duration.
The new remaining duration of the QoS session shall not exceed the maximum remaining duration limit (currently fixed at 86,400 seconds) where the remaining duration is calculated as the difference between the `expiresAt` and current time when the request to extend the session duration is received. If this maximum limit would be exceeded, the overall duration shall be set such that the remaining duration is equal to this limit.
An example: A QoD session was originally created with duration 80,000 seconds. 10,000 seconds later, the developer requested to extend the session by 20,000 seconds.
- Original duration: 80,000 seconds
- Elapsed time: 10,000 seconds
- Remaining duration: 70,000 seconds
- New remaining duration: 86,400 seconds (the maximum allowed)
- New overall session duration: 96,400 seconds
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.extend_session(
    session_id="sessionId",
    requested_additional_duration=60,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID that was obtained from the createSession operation
    
</dd>
</dl>

<dl>
<dd>

**requested_additional_duration:** `int` — Additional duration in seconds to be extended.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">get_session</a>(...) -> GetSessionQodResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Querying for QoS session resource information details
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.get_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID that was obtained from the createSession operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">delete_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Release resources related to QoS session

If the notification callback is provided and the `qosStatus` of the session was `AVAILABLE` the client will receive in addition to the response a `QOS_STATUS_CHANGED` event with
- `qosStatus` as `UNAVAILABLE` and
- `statusInfo` as `DELETE_REQUESTED`
There will be no notification event if the `qosStatus` was already `UNAVAILABLE`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.delete_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID that was obtained from the createSession operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.qod.<a href="src/networkAsCode/qod/client.py">retrieve_sessions</a>(...) -> typing.List[RetrieveSessionsQodResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all QoD sessions related to the specified device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.qod import RetrieveSessionsQodRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.qod.retrieve_sessions(
    device=RetrieveSessionsQodRequestDevice(
        phone_number="+99999991001",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `RetrieveSessionsQodRequestDevice` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DeviceSwap
<details><summary><code>client.device_swap.<a href="src/networkAsCode/device_swap/client.py">check</a>(...) -> CheckDeviceSwapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if device swap has been performed during a past period
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_swap.check(
    phone_number="+99999991000",
    max_age=120,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Optional[typing.Any]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Period in hours to be checked for device swap.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device_swap.<a href="src/networkAsCode/device_swap/client.py">retrieve_date</a>(...) -> RetrieveDateDeviceSwapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get timestamp of last device swap for a mobile user account provided with phone number.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.device_swap.retrieve_date(
    phone_number="+99999991001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Optional[typing.Any]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Geofencing
<details><summary><code>client.geofencing.<a href="src/networkAsCode/geofencing/client.py">list_subscriptions</a>(...) -> typing.List[ListSubscriptionsGeofencingResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of geofencing event subscription(s)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.geofencing.list_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.geofencing.<a href="src/networkAsCode/geofencing/client.py">create_subscription</a>(...) -> CreateSubscriptionGeofencingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a subscription for a device to receive notifications when a device enters or exits a specified area
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.geofencing import CreateSubscriptionGeofencingRequestConfig, CreateSubscriptionGeofencingRequestConfigSubscriptionDetail, CreateSubscriptionGeofencingRequestConfigSubscriptionDetailDevice, CreateSubscriptionGeofencingRequestConfigSubscriptionDetailArea
import datetime

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.geofencing.create_subscription(
    protocol="HTTP",
    sink="https://notificationSendServer12.supertelco.com",
    types=[
        "org.camaraproject.geofencing-subscriptions.v0.area-entered"
    ],
    config=CreateSubscriptionGeofencingRequestConfig(
        subscription_detail=CreateSubscriptionGeofencingRequestConfigSubscriptionDetail(
            device=CreateSubscriptionGeofencingRequestConfigSubscriptionDetailDevice(
                phone_number="+99999991000",
            ),
            area=CreateSubscriptionGeofencingRequestConfigSubscriptionDetailArea(
                area_type="CIRCLE",
            ),
        ),
        subscription_expire_time=datetime.datetime.fromisoformat("2045-03-22T05:40:58+00:00"),
        subscription_max_events=10,
        initial_event=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**protocol:** `CreateSubscriptionGeofencingRequestProtocol` — Identifier of a delivery protocol. Only HTTP is allowed for now
    
</dd>
</dl>

<dl>
<dd>

**sink:** `str` — The address to which events shall be delivered using the selected protocol.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.List[CreateSubscriptionGeofencingRequestTypesItem]` 

Camara Event types eligible to be delivered by this subscription.
Note: As of now we enforce to have only event type per subscription.
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateSubscriptionGeofencingRequestConfig` 

Implementation-specific configuration parameters needed by the subscription manager for acquiring events.
In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`
Specific event type attributes must be defined in `subscriptionDetail`
Note: if a request is performed for several event type, all subscribed event will use same `config` parameters.
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**sink_credential:** `typing.Optional[CreateSubscriptionGeofencingRequestSinkCredential]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.geofencing.<a href="src/networkAsCode/geofencing/client.py">get_subscription</a>(...) -> GetSubscriptionGeofencingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

retrieve Geofencing subscription information for a given subscription ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.geofencing.get_subscription(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.geofencing.<a href="src/networkAsCode/geofencing/client.py">delete_subscription</a>(...) -> typing.Optional[DeleteSubscriptionGeofencingResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

delete a given Geofencing subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.geofencing.delete_subscription(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — Subscription identifier that was obtained from the create event subscription operation
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Oauth
<details><summary><code>client.oauth.<a href="src/networkAsCode/oauth/client.py">get_client_credentials</a>() -> GetClientCredentialsOauthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Getting client credentials for user. If it exists that is returned, otherwise new created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.oauth.get_client_credentials()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CallForwardingSignal
<details><summary><code>client.call_forwarding_signal.<a href="src/networkAsCode/call_forwarding_signal/client.py">retrieve_call_forwarding</a>(...) -> typing.List[RetrieveCallForwardingCallForwardingSignalResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint provides information about wich type of call forwarding service is active. More than one service can be active, e.g. conditional and unconditional. This endpoit exceeds the main scope of the CFS API, for this reason an error code 501 can be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.call_forwarding_signal.retrieve_call_forwarding(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    phone_number="+99999991111",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.call_forwarding_signal.<a href="src/networkAsCode/call_forwarding_signal/client.py">retrieve_unconditional_call_forwarding</a>(...) -> RetrieveUnconditionalCallForwardingCallForwardingSignalResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint provides information about the status of the unconditional call forwarding, beeing active or not.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.call_forwarding_signal.retrieve_unconditional_call_forwarding(
    correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
    phone_number="+99999991000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**correlator:** `typing.Literal` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — A public identifier addressing a telephone subscription. In mobile networks it corresponds to the MSISDN (Mobile Station International Subscriber Directory Number). In order to be globally unique it has to be formatted in international format, according to E.164 standard, prefixed with '+'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Location
<details><summary><code>client.location.<a href="src/networkAsCode/location/client.py">retrieve</a>(...) -> RetrieveLocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the area where a certain user device is localized.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.location import RetrieveLocationRequestDevice

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.location.retrieve(
    device=RetrieveLocationRequestDevice(
        phone_number="+99999991000",
    ),
    max_age=60,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `RetrieveLocationRequestDevice` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Maximum age of the location information which is accepted for the location retrieval (in seconds)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.location.<a href="src/networkAsCode/location/client.py">verify_v1</a>(...) -> VerifyV1LocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify whether the location of a device is within a requested area. The operation returns a verification result and, optionally, a match rate estimation for the location verification in percent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.location import VerifyV1LocationRequestDevice, VerifyV1LocationRequestArea

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.location.verify_v_1(
    device=VerifyV1LocationRequestDevice(
        phone_number="+99999991000",
    ),
    area=VerifyV1LocationRequestArea(
        area_type="CIRCLE",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**area:** `VerifyV1LocationRequestArea` — Base schema for all areas
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**device:** `typing.Optional[VerifyV1LocationRequestDevice]` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE1: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device
NOTE2: for the Commonalities release v0.4, we are enforcing that the networkAccessIdentifier is only part of the schema for future-proofing, and CAMARA does not currently allow its use. After the CAMARA meta-release work is concluded and the relevant issues are resolved, its use will need to be explicitly documented in the guidelines.
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — The maximum age (in seconds) for the location known by the implementation, which is accepted for the verification. Absence of maxAge means "any age" and maxAge=0 means a fresh calculation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.location.<a href="src/networkAsCode/location/client.py">verify</a>(...) -> VerifyLocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify whether the location of a device is within a requested area. The operation returns a verification result and, optionally, a match rate estimation for the location verification in percent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment
from networkAsCode.location import VerifyLocationRequestDevice, VerifyLocationRequestArea

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.location.verify(
    device=VerifyLocationRequestDevice(
        phone_number="+99999991000",
    ),
    area=VerifyLocationRequestArea(
        area_type="CIRCLE",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device:** `VerifyLocationRequestDevice` 

End-user equipment able to connect to a mobile network. Examples of devices include smartphones or IoT sensors/actuators.

The developer can choose to provide the below specified device identifiers:

* `ipv4Address`
* `ipv6Address`
* `phoneNumber`
* `networkAccessIdentifier`

NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    
</dd>
</dl>

<dl>
<dd>

**area:** `VerifyLocationRequestArea` 
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — The maximum age (in seconds) of the available location, which is accepted for the verification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Number Verification v1.0.0
<details><summary><code>client.number_verification_v100.<a href="src/networkAsCode/number_verification_v100/client.py">phone_number_share</a>(...) -> PhoneNumberShareResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the phone number so the API clients can verify the number themselves:
- It will be done for the user that has authenticated via mobile network
- It returns the authenticated user's `device phone number` associated to the access token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.number_verification_v_100.phone_number_share()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `typing.Optional[str]` — Authorization code received from the CSP
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Application state
    
</dd>
</dl>

<dl>
<dd>

**correlator:** `typing.Optional[str]` — Correlation id for the different services
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` — authorization header for token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NaC Authorization Server
<details><summary><code>client.na_c_authorization_server.<a href="src/networkAsCode/na_c_authorization_server/client.py">get_jwks</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from networkAsCode import NetworkAsCodeApi
from networkAsCode.environment import NetworkascodeApiEnvironment

client = NetworkAsCodeApi(
    api_key="<value>",
    environment=NetworkascodeApiEnvironment.DEFAULT,
)

client.na_c_authorization_server.get_jwks(
    nac_app_ref="nac_app_ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nac_app_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

