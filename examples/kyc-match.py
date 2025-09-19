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

# You can use the match_customer method with device's or custom phone number.
# If you don't provide the phone_number parameter, the code will
# use phone_number from my_device variable by default.

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

# If successful, you can access the results like so:
print(customer_match_result)

# Or
print(customer_match_result.name_match)
print(customer_match_result.name_match_score) # if provided by Operator and name_match "false"
print(customer_match_result.address_match)
