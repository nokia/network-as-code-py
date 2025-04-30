import network_as_code as nac
from fastapi import FastAPI
from typing import Optional



# We begin by creating a Network as Code client
client = nac.NetworkAsCodeClient(
   token="<your-application-key-here>"
)

# Then, create a device object for the phone number you want to check
my_device = client.devices.get(
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+3637123456"
)
# This authorization_endpoint should be requested by the end user device and not in the backend
# of your application, since the requesting device is used to determine authorization 
# for the particular device. You could, for example,
# handle this by presenting the user with a link or a button to click to initiate the redirect flow.
# You must provide a redirect_uri, where the authorization code will be delivered.
# See the fastapi example provided below.

# You can add a state value of your choosing to test for CSRF attacks. Your application then should check, 
# that the state value given to the authorization endpoint mathes the one returned to the redirect uri.
# If the state values do not match, there has likely been a CSRF attack. In this case your application
# should return a 401 Unauthorized error code.

# create callbacklink
callback = client.authorization.create_authentication_link(
    redirect_uri= "https://my-example/redirect",
    login_hint= my_device.phone_number,
    scope= "number-verification:verify", # "number-verification:device-phone-number:read" In case of getting the device phone number.
    state= "foobar"
)

# Example of a redirect_uri to use to receive the authorization code from the authorization endpoint

app = FastAPI()

@app.get("/redirect")
async def get_authorization_code(code: str, state: Optional[str]=None):
    return (f"This is you authorization code: {code}.")

# Add your authorization code here.
code = "NaC-authorization-code"


# You can use the Number Verification API with the obtained authorization code and verify device's phone number.
# This will respond with a True or False value.
verify_number_result = my_device.verify_number(code= code)

print(verify_number_result)

# The Number Verification API retieves the phone number of the used device.

device_phone_number = my_device.get_phone_number(code = code)

print(device_phone_number) # e.g. "+123456789"
