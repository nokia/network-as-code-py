import httpx
from network_as_code.models.location import CivicAddress, Location
from ..api import APIClient


class LocationAPI:

    def __init__(self, device_id):
        self.device_id = device_id
        #self.location = Location
       # self.civic_address = CivicAddress

    def getLocation(self, device_id):
        # Do something with self.param1 and self.param2
        response = httpx.get(
            url = "https://location-verification.p-eu.rapidapi.com/get",
            params = {"device_id": device_id},
            headers = {
	            "X-RapidAPI-Key": "acd2047419mshfa34a75847e0933p1fad5ejsnc0a43f8b5f4e",
	            "X-RapidAPI-Host": "location-verification.nokia-dev.rapidapi.com"
            }
            )

        return response.json()

        """
        200 response is CivicAdress and Location
        """


    def verifyLocation(self, latitude, longitude, device_id, accuracy):
        response = httpx.get(
            url = "https://location-verification.p-eu.rapidapi.com/verify",

            params = {
                "latitude":latitude,
                "longitude":longitude,
                "device_id":device_id,
                "accuracy":accuracy},

            headers = {
	            "X-RapidAPI-Key": "acd2047419mshfa34a75847e0933p1fad5ejsnc0a43f8b5f4e",
	            "X-RapidAPI-Host": "location-verification.nokia-dev.rapidapi.com"
                        }
        )
       # return response.json()
        return response.json()
