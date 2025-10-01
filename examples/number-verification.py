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
# You must provide a redirect_uri, where the authorization code and state will be delivered.
# See the fastapi example provided below.

# Add a state value of your choosing to be used as a reference to store request-specific information and to test for CSRF attacks.
# Your application then should check, 
# that the state value given to the authorization endpoint matches the one returned to the redirect uri.
# If the state values do not match, there has likely been a CSRF attack. In this case your application
# should return a 401 Unauthorized error code.
# The state value is then used in verify_number call to find the request-specific data stored previously.

# create callbacklink
callback = client.authorization.create_authorization_link(
    redirect_uri= "https://my-example/redirect",
    login_hint= my_device.phone_number,
    scope= "dpv:FraudPreventionAndDetection number-verification:verify", # "number-verification:device-phone-number:read" In case of getting the device phone number.
    state= "foobar"
)

# Example of a redirect_uri to use to receive the authorization code and the state from the authorization endpoint

app = FastAPI()

@app.get("/redirect")
async def get_authorization_code(code: str, state: Optional[str]=None):
    return (f"This is you authorization code: {code}. This is your state variable: {state}.")

# Add your authorization code here.
code = "NaC-authorization-code"
state = "App-state"


# You can use the Number Verification API with the obtained authorization code and state to verify device's phone number.
# This will respond with a True or False value.
verify_number_result = my_device.verify_number(code= code, state= state)

print(verify_number_result)

# The Number Verification API retrieves the phone number of the used device.

device_phone_number = my_device.get_phone_number(code= code, state= state)

print(device_phone_number) # e.g. "+123456789"
