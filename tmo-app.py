
import network_as_code as nac
from network_as_code.models.slice import NetworkIdentifier, SliceInfo, AreaOfService, Point, Throughput
from network_as_code.models.device import DeviceIpv4Addr

### TMO Demo Flow ###
 
# We begin by creating a Network-as-Code client
client = nac.NetworkAsCodeClient(
    token="<token>"
)

# Get TMO supplied Slice
slice_obj = client.slices.get("Slice")

# Attach Slice to dummy Device (no-op behind the scenes)
device_obj = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="+12065550100")
slice_obj.attach(device_obj, "https://notify.me/here")

# Modify Slice
client.slices.modify(
    name="Slice",
    notification_url="https://notif.fly.dev/notify",
    network_id= NetworkIdentifier(mcc="310", mnc="310"),
    slice_info=SliceInfo(service_type="eMBB", differentiator="000BB8"),
    slice_downlink_throughput=Throughput(guaranteed=25, maximum=100),
    device_uplink_throughput=Throughput(guaranteed=10,maximum=80),
    max_data_connections=420751,
    max_devices=33    
)
