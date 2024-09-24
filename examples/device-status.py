import network_as_code as nac
from datetime import datetime, timedelta, timezone
from network_as_code.models.device import DeviceIpv4Addr

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
    phone_number="36721601234567"
)

# Simply change the event_type to
# "org.camaraproject.device-status.v0.roaming-status" whenever needed.
my_subscription = client.connectivity.subscribe(
    event_type="org.camaraproject.device-status.v0.connectivity-data",
    device=my_device,
    # You can tell when the subscription is supposed to expire
    # with a date-time object
    subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
    # Use HTTPS to send notifications
    notification_url="https://example.com/notifications",
    notification_auth_token="replace-with-your-auth-token"
)

# Use this to show the roaming subscription status
print(my_subscription)

# You can also get a subscription by its ID
subscription = client.connectivity.get_subscription(my_subscription.id)

# Or check when your subscription starts/expires:
print(subscription.starts_at)
print(subscription.expires_at)

# Delete a subscription
subscription.delete()
