
import pytest

import time

from network_as_code.models.device import Device, DeviceIpv4Addr

from network_as_code.models.slice import Apps, Throughput, NetworkIdentifier, SliceInfo, AreaOfService, Point, TrafficCategories

from network_as_code.errors import NotFound
import random
import httpx

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@testcsp.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="+3670123456")
    return device

@pytest.fixture
def setup_and_cleanup_slice_data(client):
    slice = client.slices.create(
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="444444"),
        notification_url="https://notify.me/here",
        notification_auth_token="my-token",
        name=f'slice{random.randint(1, 1000)}'
    )

    yield slice

    # If a slice was activated but the test failed before deactivation, we need to manually deactivate
    if slice.state == "OPERATING":
        slice.deactivate()
        while slice.state == "OPERATING":
            time.sleep(5)
            slice.refresh()

    slice.delete()

def test_getting_slices(client):
    assert type(client.slices.get_all()) is list

def test_creating_a_slice(client, setup_and_cleanup_slice_data):
    slice = setup_and_cleanup_slice_data
    
    assert slice.network_identifier.mnc == '30'
    assert slice.network_identifier.mcc == '236'

@pytest.mark.skip
@pytest.mark.asyncio
async def test_modifying_a_slice(client, setup_and_cleanup_slice_data):
    my_slice = setup_and_cleanup_slice_data

    await my_slice.wait_for(desired_state="AVAILABLE")

    my_slice.modify(
        max_devices=10,
        max_data_connections=20
    )

    assert my_slice.max_devices == 10
    assert my_slice.max_data_connections == 20

def test_creating_a_slice_with_optional_args(client,notification_base_url):
    slice = client.slices.create(
        name=f'slice{random.randint(1, 1000)}',
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

def test_getting_a_slice(client, setup_and_cleanup_slice_data):
    new_slice = setup_and_cleanup_slice_data

    fetched_slice = client.slices.get(new_slice.name)

    assert new_slice.sid == fetched_slice.sid


def test_deleting_a_slice_marks_it_as_deleted(client, setup_and_cleanup_slice_data):
    slice = setup_and_cleanup_slice_data

    slice.delete()

    slice.refresh()

    assert slice.state == "DELETED"

def test_getting_attachments(client):
    assert type(client.slices.get_all_attachments()) is list



# NOTE: This test takes a long time to execute, since it must wait for slice updates
#       if you are in a rush, add a temporary skip here
# @pytest.mark.skip
@pytest.mark.asyncio
async def test_deactivating_and_deleting_a_slice(client, setup_and_cleanup_slice_data):
    slice = setup_and_cleanup_slice_data

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

    slice.activate()

    await slice.wait_for(desired_state="OPERATING")

    assert slice.state == "OPERATING"
    
    slice.deactivate()

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

# NOTE: This test takes a long time to execute, since it must wait for slice updates
#       if you are in a rush, add a temporary skip here
@pytest.mark.skip
@pytest.mark.asyncio
async def test_attach_device_to_slice_and_detach(client, device, setup_and_cleanup_slice_data):
    slice = setup_and_cleanup_slice_data

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

    slice.activate()

    await slice.wait_for(desired_state="OPERATING")

    assert slice.state == "OPERATING"

    new_attachment = slice.attach(device, traffic_categories=TrafficCategories(apps=Apps(
        os="97a498e3-fc92-5c94-8986-0333d06e4e47",
        apps=["ENTERPRISE"]
    )), notification_url="https://example.com/notifications",
    notification_auth_token="c8974e592c2fa383d4a3960714")
    
    time.sleep(30)

    attachment = client.slices.get_attachment(new_attachment['nac_resource_id'])

    assert attachment['nac_resource_id'] == new_attachment['nac_resource_id']

    slice.detach(device)

    slice.deactivate()

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

# NOTE: This test takes a long time to execute, since it must wait for slice updates
#       if you are in a rush, add a temporary skip here
@pytest.mark.skip
@pytest.mark.asyncio
async def test_attach_device_to_slice_with_mandatory_params(client, device, setup_and_cleanup_slice_data):
    slice = setup_and_cleanup_slice_data

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

    slice.activate()

    await slice.wait_for(desired_state="OPERATING")

    assert slice.state == "OPERATING"

    device = client.devices.get(phone_number="+12065550100")

    new_attachment = slice.attach(device)
    
    time.sleep(30)

    attachment = client.slices.get_attachment(new_attachment['nac_resource_id'])

    assert attachment['nac_resource_id'] == new_attachment['nac_resource_id']

    slice.detach(device)

    slice.deactivate()

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

# NOTE: This test takes a long time to execute, since it must wait for slice updates
#       if you are in a rush, add a temporary skip here
@pytest.mark.skip
@pytest.mark.asyncio
async def test_attach_device_to_slice_with_optional_params(client, device, setup_and_cleanup_slice_data):
    slice = setup_and_cleanup_slice_data

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

    slice.activate()

    await slice.wait_for(desired_state="OPERATING")

    assert slice.state == "OPERATING"

    device = client.devices.get(phone_number="+12065550100")

    new_attachment = slice.attach(device,
                                  traffic_categories=TrafficCategories(apps=Apps(
                                  os="97a498e3-fc92-5c94-8986-0333d06e4e47",
                                  apps=["ENTERPRISE"])), 
                                  notification_url="https://example.com/notifications",
                                  notification_auth_token="c8974e592c2fa383d4a3960714")
    
    time.sleep(30)

    attachment = client.slices.get_attachment(new_attachment['nac_resource_id'])

    assert attachment['nac_resource_id'] == new_attachment['nac_resource_id']

    slice.detach(device)

    slice.deactivate()

    await slice.wait_for(desired_state="AVAILABLE")

    assert slice.state == "AVAILABLE"

@pytest.mark.asyncio
async def test_notifications(client, notification_base_url):
    slice = client.slices.create(
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="444444"),
        notification_url=f"{notification_base_url}/notify",
        notification_auth_token="my-token",
        name=f'slice{random.randint(1, 1000)}'
    )

    await slice.wait_for(desired_state="AVAILABLE")

    notification = httpx.get(f"{notification_base_url}/network-slice/get/{slice.name}")
    assert notification.json()['current_slice_state'] == "AVAILABLE"

    slice.activate()

    await slice.wait_for(desired_state="OPERATING")

    notification = httpx.get(f"{notification_base_url}/network-slice/get/{slice.name}")
    assert notification.json()['current_slice_state'] == "OPERATING"

    slice.deactivate()

    await slice.wait_for(desired_state="AVAILABLE")

    notification = httpx.get(f"{notification_base_url}/network-slice/get/{slice.name}")
    assert notification.json()['current_slice_state'] == "AVAILABLE"

    slice.delete()

    await slice.wait_for(desired_state="DELETED")

    notification = httpx.get(f"{notification_base_url}/network-slice/get/{slice.name}")
    assert notification.json()['current_slice_state'] == "DELETED"

    httpx.delete(f"{notification_base_url}/network-slice/delete/{slice.name}")

def test_NotFound_error(client):
    with pytest.raises(NotFound):
        client.slices.get('nonexistentsliceid')
