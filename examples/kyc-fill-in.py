import network_as_code as nac

# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
   token="<your-application-key-here>"
)

# To use the request_customer_info method you must provide the customer's phone number.

result = client.kyc.request_customer_info(
    phone_number="+99999991000",
    )

# If successful, you can access the results like so:
print(result)

# Or
print(result.id_document)
print(result.id_document_type)
print(result.country_of_birth)
print(result.nationality)
