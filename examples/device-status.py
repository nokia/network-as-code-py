import network_as_code as nac
from datetime import datetime, timedelta, timezone
from network_as_code.models.device import DeviceIpv4Addr
from network_as_code.models.device_status import EventType, AccessTokenCredential

# We begin by creating a Network as Code client
client = nac.NetworkAsCodeClient(
    token="<your-application-key-here>"
)

# Then, we create an object for the mobile device we want to use
my_device = client.devices.get(
    "device@testcsp.net",
    ipv4_address=DeviceIpv4Addr(
        public_address="192.0.2.3",
        private_address="192.0.2.204",
        public_port=80
    ),
    ipv6_address="2001:db8:1234:5678:9abc:def0:fedc:ba98",
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+3637123456"
)

# Simply change the event_type to
# [EventType.ROAMING_STATUS] whenever needed.
my_subscription = client.device_status.subscribe(
    event_type=[EventType.REACHABILITY_DATA],
    device=my_device,
    max_num_of_reports=5,
    # You can tell when the subscription is supposed to expire
    # with a date-time object
    subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
    # Use HTTPS to send notifications
    sink="https://example.com/notifications",
    sink_credential=AccessTokenCredential(
        access_token= "some-access-token",
        access_token_expires_utc= datetime.now(timezone.utc) + timedelta(days=1),
        access_token_type="bearer"
        ),
    initial_event=True
)

# Use this to show the subscription status
print(my_subscription)

# You can also get a subscription by its ID
reachability_subscription = client.device_status.get_reachability_subscription(my_subscription.id)

# Alternatively, if you created a roaming subscription
roaming_subscription = client.device_status.get_roaming_subscription(my_subscription.id)

# Or check when your subscription starts/expires:
print(my_subscription.starts_at)
print(my_subscription.expires_at)

# Delete a subscription
my_subscription.delete()
