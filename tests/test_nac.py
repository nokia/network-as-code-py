import pytest
from dateutil.parser import parse
from hypothesis import given, settings, strategies as st, HealthCheck
from network_as_code import NetworkProfile, Device, GeoZone
from network_as_code.errors import GatewayConnectionError

API_PATH = "https://apigee-api-test.nokia-solution.com/nac"


@pytest.fixture
def device():
    return Device("example@example.com", "random_api_token")


def test_device_init():
    test_id = "example@example.com"
    test_sdk_token = "random_api_token"
    test_device = Device(test_id, test_sdk_token)
    assert test_device.id == test_id
    assert test_device.sdk_token == test_sdk_token


def test_mocked_api_connection(requests_mock, device):
    requests_mock.get(f"{API_PATH}/hello", json={"service": "up"})
    assert device.check_api_connection()


@given(
    latitude=st.floats(min_value=-90, max_value=90),
    longitude=st.floats(min_value=-180, max_value=180),
    elevation=st.floats(min_value=0, max_value=1000),
    # timestamp=st.floats(allow_nan=False),
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_successful_device_location(
    requests_mock,
    device,
    latitude,
    longitude,
    elevation,  # timestamp
):
    # Register a mocked response
    timestamp = "2022-03-08T17:12:00Z"
    requests_mock.post(
        f"{API_PATH}/subscriber/location",
        json={
            "eventTime": timestamp,
            "ueId": "todd.levi@nokia.com",
            "locationInfo": {
                "ageOfLocationInfo": "2038",
                "trackingAreaId": "3100120016A8",
                "plmnId": "310012",
                "lat": str(latitude),
                "long": str(longitude),
                "elev": str(elevation),
            },
        },
    )

    # Get the device location
    lat, lon, elev, ts = device.location()

    # Assert that the data is received and parsed correctly
    assert lat == latitude
    assert lon == longitude
    assert elev == elevation
    assert ts == parse(timestamp)


def test_geozone_notification(device):
    geozone = GeoZone(device, area="Some Area")
    geozone_events = geozone.monitor()
    for event in geozone_events:
        assert event == "enter" or event == "leave"


def test_successful_network_profile_selection(requests_mock, device):
    requests_mock.patch(f"{API_PATH}/subscriber/bandwidth", text="")
    network_profile = NetworkProfile("gold")
    device.apply(network_profile)
    assert network_profile.bandwidth_profile == "gold"


def test_unsuccessful_network_profile_selection(requests_mock, device):
    requests_mock.patch(f"{API_PATH}/subscriber/bandwidth", status_code=404)
    try:
        network_profile = NetworkProfile("gold")
        device.apply(network_profile)
        # Exception should have been thrown
        assert False
    except GatewayConnectionError:
        assert True


def test_network_profile_selection_using_setter_updates_value(requests_mock, device):
    network_profile = NetworkProfile("gold")
    network_profile.bandwidth_profile = "bronze"
    assert network_profile.bandwidth_profile == "bronze"


def test_network_profile_selection_produces_correct_json_body(requests_mock):
    device = Device(sdk_token="blah", id="example@example.com")
    requests_mock.patch(f"{API_PATH}/subscriber/bandwidth", text=_json_body_callback)
    network_profile = NetworkProfile("gold")
    device.apply(network_profile)
    assert network_profile.bandwidth_profile == "gold"


def _json_body_callback(request, context):
    json_body = request.json()
    assert json_body["id"] == "example@example.com"
    assert json_body["bandwidthID"] == "gold"
    context.status_code = 200
    return ""
