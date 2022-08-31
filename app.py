import network_as_code as nac

client = nac.NetworkAsCodeClient(
    token="testing",
    base_url="http://localhost:5050/nwac/v4",
    testmode=True
)

print("Client connected:", client.connected())
print("Creating a test user")

device = client.subscriptions.create(
    id="test.user@domain.tld",
    imsi="123456789012345",
    msisdn="1234567890",
)

print("Created.")

location = device.get_location()

print(location)
