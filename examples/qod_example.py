# QoD functionalities

# QoS session examples:

import network_as_code as nac

from network_as_code.models.device import DeviceIpv4Addr

client = nac.NetworkAsCodeClient("<your-application-key-here>")

# Identify the device with its ID,
# IP address(es) and optionally, a phone number
device = client.devices.get(
    "device@testcsp.net",
    ipv4_address = DeviceIpv4Addr(
        public_address="233.252.0.2",
        private_address="192.0.2.25",
        public_port=80),
    ipv6_address = "2001:db8:1234:5678:9abc:def0:fedc:ba98",
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number = "+3672123456"
)

# Create a QoD session with QOS_L (large bandwidth) that lasts for 3,600 seconds (1 hour):
my_session = device.create_qod_session(
    service_ipv4="233.252.0.2",
    service_ipv6="2001:db8:1234:5678:9abc:def0:fedc:ba98",
    profile="QOS_L",
    duration=3600
)

# Show a list of all of the QoD sessions associated with a device
print(device.sessions())
# You can also show the duration of a given sssion
print(my_session.duration())
# Or use these to check when your session started/expires:
print(my_session.started_at)
print(my_session.expires_at)

# Get a session by its ID
session = client.sessions.get(my_session.id)

# Delete a session
my_session.delete()

# Delete all QoD sessions associated with a particular device
device.clear_sessions()
