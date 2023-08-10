import httpx
from pytest_httpx import httpx_mock
from network_as_code.api.location_api import LocationAPI
from network_as_code.models.location import CivicAddress, Location

import pytest
#import httpx-mock


@pytest.fixture
def location_api():
    return LocationAPI(device_id="test_device_id")

def test_get_location(httpx_mock: httpx_mock, location_api):
    url = "https://location-verification.p-eu.rapidapi.com/get?device_id=test_device_id"
    params = {"device_id": "test_device_id"}
    headers = {"X-RapidAPI-Key": "acd2047419mshfa34a75847e0933p1fad5ejsnc0a43f8b5f4e", "X-RapidAPI-Host": "location-verification.nokia-dev.rapidapi.com"}


    mock_response = {
        "point": {"lon": 0, "lat": 0},
        "civicAddress": {"country": "", "A1": "", "A2": "", "A3": "", "A4": "", "A5": "", "A6": ""}
    }
    httpx_mock.add_response(
        url=url, 
        method='GET', 
        headers=headers,
        json=mock_response
    )

    response = location_api.getLocation(device_id="test_device_id")
    assert response == mock_response

def test_verify_location(httpx_mock: httpx_mock, location_api):
   
    params = {
        "latitude":"test_latitude",
        "longitude":"test_longitude",
        "device_id":"test_device_id",
        "accuracy":"test_accuracy"
        }
    url = f"https://location-verification.p-eu.rapidapi.com/verify?latitude={params['latitude']}&longitude={params['longitude']}&device_id={params['device_id']}&accuracy={params['accuracy']}"

    headers = {
        "X-RapidAPI-Key": "acd2047419mshfa34a75847e0933p1fad5ejsnc0a43f8b5f4e", 
        "X-RapidAPI-Host": "location-verification.nokia-dev.rapidapi.com"
    }

    httpx_mock.add_response(
        url=url, 
        method='GET', 
        #params=params,  # <-- Added this line to ensure mock matches the request based on query params
        headers=headers,
        json={"message": "Success"}
    )

    response = location_api.verifyLocation(
        latitude="test_latitude", 
        longitude="test_longitude", 
        device_id="test_device_id", 
        accuracy="test_accuracy"
    )
    #content = response.json()

    assert response == {"message": "Success"}
