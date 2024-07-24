# Network Insights functionalities

# Congestion examples:

import network_as_code as nac

from datetime import datetime, timezone, timedelta

from network_as_code.models.device import Device, DeviceIpv4Addr

# Initialize the client object with your application key
SDK_TOKEN = "<replace-me>"
DEVICE_ID = "device@testcsp.net"

# Give the device the device identifier and SDK token
client = nac.NetworkAsCodeClient(
    token=SDK_TOKEN
)

my_device = client.devices.get(DEVICE_ID)

# Subscribe your device to Congestion notifications
congestion_subscription = client.insights.subscribe_to_congestion_info(
    my_device,
    # Set the duration of your subscription to congestion insights,
    # e.g.: it can end in `n` days starting from now.
    subscription_expire_time=datetime.now(timezone.utc) + timedelta(days=1),
    # Set a notification URL with auth token to receive updates
    notification_url="https://example.com/notify",
    notification_auth_token="my-secret-token"
)

# Subscriptions are identified by id, for management
# Use this to show the subscription:
print(congestion_subscription.id)

# Or check when your subscription starts/expires:
print(congestion_subscription.starts_at)
print(congestion_subscription.expires_at)

# Get historical data between two timestamps
# Set the duration/time difference with the timedelta function
congestion = my_device.get_congestion(
    start=datetime.now(timezone.utc),
    end=datetime.now(timezone.utc) + timedelta(hours=3)
)
