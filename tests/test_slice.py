
from network_as_code.models.slice import Throughput, NetworkIdentifier, SliceInfo, AreaOfService, Point

def test_creating_a_slice(client):
    slice = client.slices.create(
        name="testslice",
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
        notification_url="https://notify.me/here",
        notification_auth_token="my-token",
        max_data_connections=12,
        max_devices=3
    )

    assert slice.name == 'testslice'
    # slice.delete()

def test_creating_a_slice_with_optional_args(client):
    slice = client.slices.create(
        name="mySliceName",
        network_id=NetworkIdentifier(mcc="236", mnc="30"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
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
        name="slicefour",
        network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
        notification_url="https://notify.me/here",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )

    fetched_slice = client.slices.get(new_slice.sid)

    assert new_slice.sid == fetched_slice.sid

    new_slice.delete()

# def test_activating_and_attaching_a_slice(client):
#     device = client.devices.get("testdevice@nokia.com")

    # slice = client.slices.create(
    #     network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
    #     slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
    #     area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
    #     notification_url="https://notify.me/here"
    # )

#     def on_creation_handler(slice):
#         slice.activate()
#         slice.attach()

#     slice.on_creation(on_creation_handler)

# def test_logging_a_slice(client):
#     device = client.devices.get("testdevice@nokia.com")

    # slice = client.slices.create(
    #     network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
    #     slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
    #     area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
    #     notification_url="https://notify.me/here"
    # )

#     def event_logger(slice, message):
#         print(message)

#     slice.on_event(event_logger)

def test_deactivating_and_deleting_a_slice(client):
    slice = client.slices.create(
        network_id=NetworkIdentifier(mcc="358ffYYT", mnc="246fsTRE"),
        slice_info=SliceInfo(service_type="eMBB", differentiator="44eab5"),
        area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
        notification_url="https://notify.me/here"
    )

    slice.activate()
    
    slice.deactivate()

    slice.delete()

