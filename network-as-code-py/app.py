
import os

from network_as_code import NetworkAsCodeApi
from network_as_code.location import (
    RetrieveLocationRequestDevice,
)    

client = NetworkAsCodeApi(
    rapidapi_host="network-as-code.nokia.rapidapi.com",
    api_key=os.environ["API_KEY"]
)

print(client.location.retrieve(
    device={
        "phone_number": "+99999991000"
    },
    max_age=60
))
