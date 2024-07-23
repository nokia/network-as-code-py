# Device Status functionalities

# Subscribing to Connectivity and Roaming updates:

from typing import List
import network_as_code as nac

from network_as_code.models.device import Device, DeviceIpv4Addr

client = nac.NetworkAsCodeClient(
    token="<your-application-key-here>"
)

device = client.devices.get(
    "device@bestcsp.net",
    ipv4_address = DeviceIpv4Addr(
        public_address="233.252.0.2",
        private_address="192.0.2.25",
        public_port=80),
    ipv6_address = "2001:db8:1234:5678:9abc:def0:fedc:ba98",
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number = "36721601234567"
)

connectivity_subscription = client.connectivity.subscribe(
    # Change it to "ROAMING_STATUS" whenever needed
    event_type="CONNECTIVITY",
    device=device,
    max_num_of_reports=5,
    notification_url="https://example.com/notifications",
    # Use HTTPS to send notifications
    notification_auth_token="replace-with-your-auth-token"
)

# Get a subscription by its ID
subscription = client.connectivity.get_subscription(connectivity_subscription.id)

# Delete a subscription
connectivity_subscription.delete()
