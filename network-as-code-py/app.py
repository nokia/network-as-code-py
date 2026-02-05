
import os

from network_as_code import NetworkAsCodeApi
from network_as_code.location_retrieval_v_020 import (
    RetrieveLocationRequestDevice,
)    

client = NetworkAsCodeApi(
    rapidapi_host="network-as-code.nokia.rapidapi.com",
    api_key=os.environ["API_KEY"]
)

print(client.location_retrieval_v_020.retrieve_location(
    device=RetrieveLocationRequestDevice(
        phone_number="+99999991000"
    ),
    max_age=60
))
