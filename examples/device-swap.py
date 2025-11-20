import network_as_code as nac


# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
    token="<your-application-key-here>",
)

# Then, create a device object for the phone number you want to check
my_device = client.devices.get(
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+3637123456"
)

# The date of the last device swap can be retrieved like so:
# The output may be None, if no Device Swap has occurred.
# Or it may also return the SIM installation date.
device_swap_date = my_device.get_device_swap_date()

# Otherwise it behaves like a regular datetime object
print(f"Last device swap (or SIM installation) happened on {device_swap_date.isoformat()}")


# It is also possible to check if a device swap has occurred in general
if my_device.verify_device_swap():
    print("A device swap has occurred!")


# If we want to check if it occurred in the last `n` hours:
if my_device.verify_device_swap(max_age=1):
    print("A device swap has occurred within the past hour!")
