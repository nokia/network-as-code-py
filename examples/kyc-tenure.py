import network_as_code as nac

# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
   token="<your-application-key-here>"
)

# To use the check_tenure method you must provide the customer's phone number.

# Add the tenure date from which the continuous tenure of the subscriber is to be confirmed

result = client.kyc.check_tenure(
    phone_number="+99999991000",
    tenure_date="2023-03-17"
)

# If successful, you can access the results like so:
print(result)

# Or
print(result.tenure_date_check)
print(result.contract_type)
