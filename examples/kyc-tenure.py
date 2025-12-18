import network_as_code as nac
from datetime import (
    datetime,
    timedelta,
    timezone,
    date
)

# Initialize the client object with your application key
client = nac.NetworkAsCodeClient(
   token="<your-application-key-here>"
)

# To use the check_tenure method you must provide the customer's phone number.

# Add the tenure date from which the continuous tenure of the subscriber is to be confirmed
# For example, to check a year long tenure:

result = client.kyc.check_tenure(
    phone_number="+99999991000",
    # You can also use date(YYYY, MM, DD) or a string value 'YYYY-MM-DD'
    tenure_date=datetime.now(timezone.utc) - timedelta(days=365)
)

# If successful, you can access the results like so:
print(result)

# Or
print(result.tenure_date_check)
print(result.contract_type)
