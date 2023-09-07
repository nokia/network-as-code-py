import httpx

from ..errors import error_handler

class LocationAPI:
    def __init__(self, base_url: str, rapid_key:str, rapid_host: str):
        self.client = httpx.Client(
            base_url=base_url, 
            headers={"X-RapidAPI-Host": rapid_host, "X-RapidAPI-Key": rapid_key
        })

    def get_location(self, device_id):
        response = self.client.get(
            url = "/get",
            params = {"device_id": device_id},
        )

        error_handler(response)

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
