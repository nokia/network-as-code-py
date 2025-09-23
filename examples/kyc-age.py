import network_as_code as nac

# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
   token="<your-application-key-here>"
)

# Then, create a device object for the phone number you want to check
my_device = client.devices.get(
    # The phone number accepts the "+" sign, but not spaces or "()" marks
    phone_number="+999999991000"
)

# You can use the age_verify method with device's or custom phone number.
# If you don't provide the phone_number parameter, the code will
# use phone_number from my_device variable by default

# Add age_threshold in the request to check if the age of the subscriber is older than that
# Other additional identifying parameters can be used to confirm that the subscriber is the contract's owner

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

