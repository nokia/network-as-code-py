import network_as_code as nac

# We begin by creating a Network as Code client
client = nac.NetworkAsCodeClient(
    token="<your-application-key-here>"
)

# Then, create a device object for the phone number you want to check
my_device = client.devices.get(
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+3637123456"
)

# Verify, if a device has an active, unconditional call forwarding
result = my_device.verify_unconditional_forwarding()

# Show the result
print(result)

# To get information about an active "call forwarding setup" for the given device,
# use the following snippet:
service_list = my_device.get_call_forwarding()

# Show active Call Forwarding Services
print(service_list)