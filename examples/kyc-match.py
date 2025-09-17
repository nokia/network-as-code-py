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

# You can use the match_customer method with or without an authorization code.
# In this case the device phone number is required to be provided in the parameters.

# Add the customer identity data, which is to be used in matching
# a customer against the account data bound to their phone number.

customer_match_result = my_device.match_customer(
                phone_number= '+99999991000',
                id_document= "66666666q",
                name= "Federica Sanchez Arjona",
                given_name= "Federica",
                family_name= "Sanchez Arjona",
                name_kana_hankaku= "federica",
                name_kana_zenkaku= "Ｆｅｄｅｒｉｃａ",
                middle_names= "Sanchez",
                family_name_at_birth= "YYYY",
                address= "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
                street_name= "Nicolas Salmeron",
                street_number= "4",
                postal_code= "1028460",
                region= "Tokyo",
                locality= "ZZZZ",
                country= "JP",
                house_number_extension= "VVVV",
                birthdate= "1978-08-22",
                email= "abc@example.com",
                gender= "OTHER")

print(customer_match_result)

# Alternativelly you can retrieve an authorization code and use the code in the matchCustomer method. 
# In this case, no device phone number is required to be provided in the parameters.

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
    scope= "kyc-match:match",
    state= "foobar"
)

app = FastAPI()

@app.get("/redirect")
async def get_authorization_code(code: str, state: Optional[str]=None):
    return (f"This is you authorization code: {code}.")

# Add your authorization code here.
code = "NaC-authorization-code"

# You can use the KYC Match API with the obtained authorization code.
# The KYC Match endpoint will respond with the result of the matching for each requested attribute.
# Result values for each attribute can be true, false or not_available.

customer_match_result_with_code = my_device.match_customer(
                code= code,
                id_document= "66666666q",
                name= "Federica Sanchez Arjona",
                given_name= "Federica",
                family_name= "Sanchez Arjona",
                name_kana_hankaku= "federica",
                name_kana_zenkaku= "Ｆｅｄｅｒｉｃａ",
                middle_names= "Sanchez",
                family_name_at_birth= "YYYY",
                address= "Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
                street_name= "Nicolas Salmeron",
                street_number= "4",
                postal_code= "1028460",
                region= "Tokyo",
                locality= "ZZZZ",
                country= "JP",
                house_number_extension= "VVVV",
                birthdate= "1978-08-22",
                email= "abc@example.com",
                gender= "OTHER")

print(customer_match_result_with_code)
