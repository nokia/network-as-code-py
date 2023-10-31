
import pytest

import time

from network_as_code.models.device import Device, DeviceIpv4Addr

from network_as_code.models.slice import Throughput, NetworkIdentifier, SliceInfo, AreaOfService, Point

from network_as_code.errors import error_handler
from network_as_code.errors import AuthenticationException, NotFound, ServiceError, APIError

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="+12065550100")
    return device

def test_getting_slices(client):
    assert type(client.slices.getAll()) is list

def test_creating_a_slice(client):
    slice = client.slices.create(
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="444444"),
        notification_url="https://notify.me/here",
        notification_auth_token="my-token",
        name="sdk-integration-slice-1"
    )

    assert slice.name == "sdk-integration-slice-1"
    slice.delete()

def test_creating_a_slice_with_optional_args(client):
    slice = client.slices.create(
        name="slicemock24",
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="https://notify.me/here",
        notification_auth_token="my-token",
        slice_downlink_throughput=Throughput(guaranteed=3415, maximum=1234324), 
        slice_uplink_throughput=Throughput(guaranteed=3415, maximum=1234324),
        device_downlink_throughput=Throughput(guaranteed=3415, maximum=1234324),
        device_uplink_throughput=Throughput(guaranteed=3415, maximum=1234324),
        max_data_connections=10,
        max_devices=5
    )

    slice.delete()

def test_getting_a_slice(client):
    new_slice = client.slices.create(
        name="slicemock25",
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        notification_url="https://notify.me/here",
        notification_auth_token="my-token",
    )

    fetched_slice = client.slices.get(new_slice.name)

    assert new_slice.sid == fetched_slice.sid

    new_slice.delete()

@pytest.mark.xfail
def test_get_after_deleting_all_slices_marks_them_as_deleted(client):
    slice = client.slices.create(
        name="slicemock27",
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        notification_url="https://notify.me/here",
        notification_auth_token= "samplenotificationtoken",
    )

    for network_slice in client.slices.getAll():
        network_slice.delete()

    for network_slice in client.slices.getAll():
        assert network_slice.state == "DELETED"

@pytest.mark.xfail
def test_deactivating_and_deleting_a_slice(client):
    slice = client.slices.create(
        name="slicemock26",
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        notification_url="https://notify.me/here",
        notification_auth_token= "samplenotificationtoken",
    )

    counter = 0
    while slice.state == "PENDING" and counter < 5:
        slice.refresh()
        time.sleep(5)
        counter += 1

    assert slice.state == "AVAILABLE"

    slice.activate()

    counter = 0
    while slice.state == "AVAILABLE" and counter < 5:
        slice.refresh()
        time.sleep(5)
        counter += 1

    assert slice.state == "OPERATING"
    
    slice.deactivate()

    counter = 0
    while slice.state == "OPERATING" and counter < 5:
        slice.refresh()
        time.sleep(5)
        counter += 1

    assert slice.state == "AVAILABLE"

    slice.delete()

# def test_attach_device_to_slice_and_detach(client, device):
#     slice = client.slices.create(
#         name="slicefour",
#         network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
#         slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
#         area_of_service=AreaOfService(poligon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
#         notification_url="https://notify.me/here",
#         notification_auth_token= "samplenotificationtoken",
#         slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
#         slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
#         device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
#         device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
#         max_devices=3,
#         max_data_connections=12
#     )

#     slice.activate()

#     slice.attach(device, "https://example.org/notify")
#     slice.detach(device, "https://example.org/notify")

#     slice.deactivate()

#     slice.delete()


def test_NotFound_error(client):
    with pytest.raises(NotFound):
        client.slices.get('non_existent_slice_id')

@pytest.mark.skip(reason="Pydantic doesn't allow empty name")
def test_APIError(client):
    with pytest.raises(APIError):
        client.slices.create(
         name="",
         network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
         slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
         area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
         notification_url="https://notify.me/here",
         notification_auth_token= "my-token",
         slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
         slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
         device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
         device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
         max_devices=3,
         max_data_connections=12
     )

@pytest.mark.skip(reason="Pydantic validator is already catching the name parameter")
def test_InvalidParameter(client):
    with pytest.raises(APIError):
        client.slices.create(
         name="1234567890"*100,
         network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
         slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
         area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
         notification_url="https://notify.me/here",
         notification_auth_token= "my-token",
         slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
         slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
         device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
         device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
         max_devices=3,
         max_data_connections=12
     )
