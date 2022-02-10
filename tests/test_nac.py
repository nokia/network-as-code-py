import pytest
from hypothesis import given, settings, strategies as st, HealthCheck
from network_as_code import NetworkSlice, Device, DeviceLocation

API_PATH = "https://apigee-api-test.nokia-solution.com/network-as-code"


@pytest.fixture
def device():
    return Device("310170845466094", "random_api_token")


def test_device_init():
    test_imsi = "310170845466094"
    test_sdk_token = "random_api_token"
    test_device = Device(test_imsi, test_sdk_token)
    assert test_device.imsi == test_imsi
    assert test_device.sdk_token == test_sdk_token

def test_mocked_api_connection(requests_mock, device):
    requests_mock.get(
        f"{API_PATH}/hello",
        json={
            "service": "up"
        },
    )

    assert device.check_api_connection()

@given(
    latitude=st.floats(min_value=-90, max_value=90),
    longitude=st.floats(min_value=-180, max_value=180),
    altitude=st.floats(min_value=0, max_value=1000),
    timestamp=st.floats(allow_nan=False),
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_successful_device_location(
    requests_mock, device, latitude, longitude, altitude, timestamp
):
    # Register a mocked response
    requests_mock.get(
        f"{API_PATH}/location/{device.imsi}",
        json={
            "imsi": device.imsi,
            "location": {
                "latitude": latitude,
                "longitude": longitude,
                "altitude": altitude,
                "timestamp": timestamp,
            },
        },
    )

    # Get the device location
    device_location = DeviceLocation(device)

    # Assert that the data is received and stored correctly
    assert device_location.latitude == latitude
    assert device_location.longitude == longitude
    assert device_location.altitude == altitude
    assert device_location.timestamp == timestamp


@given(
    _id=st.integers(min_value=0),
    index=st.integers(min_value=0, max_value=7),
    qos=st.integers(min_value=0, max_value=4),
    bandwidth=st.integers(min_value=0),
    default=st.booleans(),
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_successful_network_slice_creation(
    requests_mock, device, _id, index, qos, bandwidth, default
):
    requests_mock.post(
        f"{API_PATH}/networkslices",
        json={
            "_id": _id,
            "index": index,
            "qos": qos,
            "bandwidth": bandwidth,
            "default": default,
        },
    )
    network_slice = NetworkSlice(device, index, qos, bandwidth, default)

    assert network_slice.device == device
    assert network_slice._id == _id
    assert network_slice.index == index
    assert network_slice.qos == qos
    assert network_slice.bandwidth == bandwidth
    assert network_slice.default == default
