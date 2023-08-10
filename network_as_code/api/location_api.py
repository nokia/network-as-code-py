import httpx


class LocationAPI:
    def __init__(self, token: str, base_url: str = "https://location-verification.p-eu.rapidapi.com", rapid_host: str = "location-verification.nokia-dev.rapidapi.com"):
        self.client = httpx.Client(base_url=base_url, headers={"X-RapidAPI-Host": rapid_host, "X-RapidAPI-Key": token})

    def get_location(self, device_id):
        response = self.client.get(
            url = "/get",
            params = {"device_id": device_id},
            )

        print(response)

        return response.json()

    def verify_location(self, latitude, longitude, device_id, accuracy):
        response = self.client.get(
            url = "/verify",
            params = {
                "latitude":latitude,
                "longitude":longitude,
                "device_id":device_id,
                "accuracy":accuracy},
        )
        return response.is_success
