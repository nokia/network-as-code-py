import pytest
import json
from dateutil.parser import parse
from hypothesis import given, settings, strategies as st, HealthCheck
from network_as_code import (
    NetworkProfile,
    Device,
    DeviceLocation,
    GeoZone,
    CustomNetworkProfile,
    Unit,
)
from network_as_code.errors import APIError

API_PATH = "https://apigee-api-test.nokia-solution.com/nac/v2"


@pytest.fixture
def device():
    return Device(id="example@example.com", sdk_token="random_api_token")


@pytest.fixture
def network_profile():
    return NetworkProfile(bandwidth_profile="uav_streaming")


@pytest.fixture
def custom_network_profile():
    return CustomNetworkProfile(download=50, upload=10, unit=Unit.BIT)


@pytest.fixture
def device_location():
    return DeviceLocation(
        latitude=1234.56,
        longitude=1234.56,
        elevation=1234.56,
        timestamp=parse("2022-03-08T17:12:00Z", ignoretz=True),
    )


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
    location = device.location()

    # Assert that the data is received and parsed correctly
    assert location.latitude == latitude
    assert location.longitude == longitude
    assert location.elevation == elevation
    assert location.timestamp == parse(timestamp)


def test_geozone_notification(device):
    geozone = GeoZone(device, area="Some Area")
    geozone_events = geozone.monitor()
    for event in geozone_events:
        assert event == "enter" or event == "leave"


def test_getting_current_network_profile(requests_mock, device):
    requests_mock.post(
        f"{API_PATH}/subscriber/bandwidth",
        status_code=200,
        json={
            "id": "todd.levi@nokia.com",
            "serviceTier": "uav_streaming",
            "priority": "premium",
        },
    )
    network_profile = device.network_profile()
    assert network_profile.bandwidth_profile == "uav_streaming"


def test_successful_network_profile_selection(requests_mock, device, network_profile):
    requests_mock.patch(f"{API_PATH}/subscriber/bandwidth", text="")
    device.apply(network_profile)
    assert network_profile.bandwidth_profile == "uav_streaming"


def test_api_error(requests_mock, device, network_profile):
    requests_mock.patch(f"{API_PATH}/subscriber/bandwidth", status_code=404)
    try:
        device.apply(network_profile)
        # Exception should have been thrown
        assert False
    except APIError:
        assert True


def test_network_profile_selection_using_setter_updates_value(network_profile):
    network_profile.bandwidth_profile = "uav_lowpowermode"
    assert network_profile.bandwidth_profile == "uav_lowpowermode"


def test_network_profile_selection_produces_correct_json_body(
    requests_mock, device, network_profile
):
    requests_mock.patch(f"{API_PATH}/subscriber/bandwidth", text=_json_body_callback)
    device.apply(network_profile)
    assert network_profile.bandwidth_profile == "uav_streaming"


def _json_body_callback(request, context):
    json_body = request.json()
    assert json_body["id"] == "example@example.com"
    assert json_body["bandwidth"] == "uav_streaming"
    context.status_code = 200
    return ""


def test_conversion_of_bandwidth_units():
    assert Unit.BIT.convert_from(Unit.KBIT, 50) == 50000
    assert Unit.KBIT.convert_from(Unit.MBIT, 100) == 100000
    assert Unit.BIT.convert_from(Unit.MBIT, 1) == 1000000


def test_creation_of_custom_network_profile(custom_network_profile):
    assert custom_network_profile.bandwidth_profile == "custom"


def test_applying_custom_network_profile_sends_correct_body(
    requests_mock, device, custom_network_profile
):
    requests_mock.patch(
        f"{API_PATH}/subscriber/bandwidth/custom",
        text=_json_body_callback_custom_network_profile,
    )
    device.apply(custom_network_profile)
    assert custom_network_profile.bandwidth_profile == "custom"


def _json_body_callback_custom_network_profile(request, context):
    json_body = request.json()
    assert json_body["id"] == "example@example.com"
    assert json_body["download"] == 50
    assert json_body["upload"] == 10
    context.status_code = 200
    return ""


def test_applying_custom_network_profile_unit_conversion_works(requests_mock, device):
    requests_mock.patch(
        f"{API_PATH}/subscriber/bandwidth/custom",
        text=_json_body_callback_test_unit_conversion,
    )
    network_profile = CustomNetworkProfile(download=50, upload=10, unit=Unit.MBIT)
    device.apply(network_profile)
    assert network_profile.bandwidth_profile == "custom"


def _json_body_callback_test_unit_conversion(request, context):
    json_body = request.json()
    assert json_body["download"] == 50 * 1000 * 1000
    assert json_body["upload"] == 10 * 1000 * 1000
    context.status_code = 200
    return ""


def test_object_repr_methods(
    device, device_location, network_profile, custom_network_profile
):
    assert (
        repr(device) == "Device(id='example@example.com', sdk_token='random_api_token')"
    )
    assert (
        repr(device_location)
        == "DeviceLocation(latitude=1234.56, longitude=1234.56, elevation=1234.56, timestamp=datetime.datetime(2022, 3, 8, 17, 12))"
    )
    assert (
        repr(network_profile)
        == "NetworkProfile(bandwidth_profile='uav_streaming', priority=None)"
    )
    assert (
        repr(custom_network_profile)
        == "CustomNetworkProfile(download=50, upload=10, unit=<Unit.BIT: 1>)"
    )


def test_getting_custom_network_profile(requests_mock, device):
    requests_mock.post(
        f"{API_PATH}/subscriber/bandwidth/custom",
        text=_return_custom_network_profile,
    )
    network_profile = CustomNetworkProfile.get(device)

    assert network_profile.bandwidth_profile == "custom"
    assert network_profile.download == 50
    assert network_profile.upload == 10


def _return_custom_network_profile(request, context):
    json_body = request.json()
    assert json_body["id"] == "example@example.com"
    context.status_code = 200
    return json.dumps(
        {
            "id": "example@example.com",
            "download": 50,
            "upload": 10,
        }
    )
