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
    phone_number="36721601234567"
)

# Check the latest SIM-Swap date
latest_sim_swap_date = my_device.get_sim_swap_date()

 # Check SIM-Swap events within specified time spans
# The max_age parameter is not mandatory
# This method also checks if SIM swap occurred within an undefined age
sim_swap_check = my_device.verify_sim_swap(max_age=360)
