import network_as_code as nac
from fastapi import FastAPI
from typing import Optional

# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
   token="<your-application-key-here>"
)

# Then, create a device object for the phone number you want to check
my_device = client.devices.get(
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+999999991000"
)

# You can use the age_verify method either with phone number or with authorization code.
# In this case we use the device's phone number as an identifier.

# Add age_threshold in the request to check if the age of the subscriber is older than that
# Other additional indetifying parameters can be used to confirm that the subscriber is the contract's owner

result = my_device.verify_age(
    age_threshold=18,
    phone_number="+99999991000",
    id_document="123456",
    name="Federica Sanchez Arjona",
    given_name="Federica",
    family_name="Sanchez Arjona",
    family_name_at_birth="YYYY",
    middle_names="Sanchez",
    birthdate="1978-08-22",
    email="federicaSanchez.Arjona@example.com",
    include_content_lock=True,
    include_parental_control=True
    )

# If successful, you can access the results like so:
print(result)

# Or
print(result.age_check)
print(result.verified_status)
print(result.identity_match_score)
print(result.content_lock)
print(result.parental_control)

# Alternativelly you can retrieve an authorization code and use the code in the verify_age method. 
# In this case, do not use the phone number in addition.

# This authorization_endpoint should be requested by the end user device and not in the backend
# of your application, since the requesting device is used to determine authorization 
# for the particular device. You could, for example,
# handle this by presenting the user with a link or a button to click to initiate the redirect flow.
# You must provide a redirectUri, where the authorization code will be delivered.
# See the express example provided below.

# You can add a state value of your choosing to test for CSRF attacks. Your application then should check, 
# that the state value given to the authorization endpoint matches the one returned to the redirect uri.
# If the state values do not match, there has likely been a CSRF attack. In this case your application
# should return a 401 Unauthorized error code.

# create callbacklink
callback = client.authorization.create_authentication_link(
    redirect_uri= "https://my-example/redirect",
    login_hint= my_device.phone_number,
    scope= "kyc-age:verify",
    state= "foobar"
)

app = FastAPI()

@app.get("/redirect")
async def get_authorization_code(code: str, state: Optional[str]=None):
    return (f"This is you authorization code: {code}.")

# Add your authorization code here.
code = "NaC-authorization-code"

# You can use the KYC Age API with the obtained authorization code.
# The KYC Age endpoint will respond with the result of the age verification with additional information
result = my_device.verify_age(
    age_threshold=18,
    code=code,
    id_document="123456",
    name="Federica Sanchez Arjona",
    given_name="Federica",
    family_name="Sanchez Arjona",
    family_name_at_birth="YYYY",
    middle_names="Sanchez",
    birthdate="1978-08-22",
    email="federicaSanchez.Arjona@example.com",
    include_content_lock=False,
    include_parental_control=True
    )

print(result)

