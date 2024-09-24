# Identity and security functionalities

# SIM Swap examples:

import network_as_code as nac

from network_as_code.models.device import Device

# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
    token="<your-application-key-here>",
)

# Then, create a device object for the phone number you want to check
my_device = client.devices.get(
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+346661113334"
)

# The date of the last SIM Swap can be retrieved like so:
# The output may be null, if no SIM Swap has occurred.
# Or it may also return the SIM activation date.
sim_swap_date = my_device.get_sim_swap_date()

# Otherwise it behaves like a regular datetime object
print(sim_swap_date.isoformat())

# If you are only interested if a SIM swap has occurred,
# just use:
if my_device.verify_sim_swap():
    print("There has been a SIM swap!")

# You can also test if the SIM swap happened recently:
if my_device.verify_sim_swap(max_age=3600):
    print("A SIM swap occurred within the past hour!")