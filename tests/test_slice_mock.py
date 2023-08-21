import json
import pytest
from pytest_httpx import HTTPXMock
from network_as_code.client import NetworkAsCodeClient
from network_as_code.models.slice import NetworkIdentifier, Slice, SliceInfo, AreaOfService, Point, Throughput
from network_as_code.models.device import Device, DeviceIpv4Addr


MOCK_SLICE = {
    "slice": {
            "name": "sliceone",
            "notificationUrl": "",
            "notificationAuthToken": "samplenotificationtoken",
            "networkIdentifier": {
                "mcc": "236",
                "mnc": "30"
            },
            "sliceInfo": {
                "service_type": 1,
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "poligon": [
                {
                    "lat": 47.344,
                    "lon": 104.349
                },
                {
                    "lat": 35.344,
                    "lon": 76.619
                },
                {
                    "lat": 12.344,
                    "lon": 142.541
                },
                {
                    "lat": 19.43,
                    "lon": 103.53
                }
                ]
            },
            "maxDataConnections": 12,
            "maxDevices": 3,
            "sliceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "sliceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            }
            },
            "startPollingAt": 1691482014,
            "csi_id": "csi_368",
            "order_id": "6ed9b1b3-a6c5-49c2-8fa7-5cf70ba8fc23",
            "administrativeState": None,
            "state": "inProgress"
}

def to_bytes(json_content: dict) -> bytes:
    return json.dumps(json_content).encode()

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="+12065550100")
    return device

def test_creating_a_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    slice_payload = {
        "networkIdentifier": {
            "mnc": "30",
            "mcc": "236"
        },
        "sliceInfo": {
            "service_type": "eMBB",
            "differentiator": "AAABBB"
        },
        "areaOfService": {
            "poligon": [
                    {
                        "lat": 47.344,
                        "lon": 104.349
                    },
                    {
                        "lat": 35.344,
                        "lon": 76.619
                    },
                    {
                        "lat": 12.344,
                        "lon": 142.541
                    },
                    {
                        "lat": 19.43,
                        "lon": 103.53
                    }
            ]
        },
        "notificationUrl": "",
        "name": "slicefour",
        "notificationAuthToken": "samplenotificationtoken",
        "maxDataConnections": 12,
        "maxDevices": 3,
        "sliceDownlinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        },
        "sliceUplinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        },
        "deviceUplinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        },
        "deviceDownlinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        }
    }

    slice_response = {
        "slice": {
            "name": "slicefour",
            "notificationUrl": "",
            "notificationAuthToken": "samplenotificationtoken",
            "networkIdentifier": {
                "mcc": "236",
                "mnc": "30"
            },
            "sliceInfo": {
                "service_type": 1,
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "poligon": [
                {
                    "lat": 47.344,
                    "lon": 104.349
                },
                {
                    "lat": 35.344,
                    "lon": 76.619
                },
                {
                    "lat": 12.344,
                    "lon": 142.541
                },
                {
                    "lat": 19.43,
                    "lon": 103.53
                }
                ]
            },
            "maxDataConnections": 12,
            "maxDevices": 3,
            "sliceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "sliceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            }
            },
            "startPollingAt": 1691482014,
            "csi_id": "csi_989",
            "order_id": "6ed9b1b3-a6c5-49c2-8fa7-5cf70ba8fc23",
            "administrativeState": None,
            "state": "PENDING"
    }

    httpx_mock.add_response(
        method="POST",
        match_content=to_bytes(slice_payload),
        json=slice_response,
        url="https://network-slicing.p-eu.rapidapi.com/slices"
    )

    """
b'{"networkIdentifier": {"mnc": "30", "mcc": "236"}, "sliceInfo": {"service_type": "eMBB", "differentiator": "AAABBB"}, "areaOfService": {"poligon": [{"longitude": 104.349, "latitude": 47.344}, {"longitude": 76.619, "latitude": 35.344}, {"longitude": 142.541, "latitude": 12.344}, {"longitude": 103.53, "latitude": 19.43}]}, "notificationUrl": "", "name": "slicefour", "notificationAuthToken": "samplenotificationtoken", "maxDataConnections": 12, "maxDevices": 3, "sliceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "sliceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}}' body amongst:
b'{"networkIdentifier": {"mnc": "30", "mcc": "236"}, "sliceInfo": {"service_type": "eMBB", "differentiator": "AAABBB"}, "areaOfService": {"poligon": [{"lat": 47.344, "lon": 104.349}, {"lat": 35.344, "lon": 76.619}, {"lat": 12.344, "lon": 142.541}, {"lat": 19.43, "lon": 103.53}]}, "notificationUrl": "", "name": "slicefour", "notificationAuthToken": "samplenotificationtoken", "maxDataConnections": 12, "maxDevices": 3, "sliceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "sliceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}}' body
    """

    slice = client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(poligon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )
    assert slice.name == slice_payload['name']
    assert slice.state == slice_response['state']

def test_modifying_a_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    slice_payload = {
        "networkIdentifier": {
            "mnc": "30",
            "mcc": "236"
        },
        "sliceInfo": {
            "service_type": "eMBB",
            "differentiator": "AAABBB"
        },
        "areaOfService": {
            "poligon": [
                    {
                        "lat": 47.344,
                        "lon": 104.349
                    },
                    {
                        "lat": 35.344,
                        "lon": 76.619
                    },
                    {
                        "lat": 12.344,
                        "lon": 142.541
                    },
                    {
                        "lat": 19.43,
                        "lon": 103.53
                    }
            ]
        },
        "notificationUrl": "",
        "name": "slicefour",
        "notificationAuthToken": "samplenotificationtoken",
        "maxDataConnections": 12,
        "maxDevices": 3,
        "sliceDownlinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        },
        "sliceUplinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        },
        "deviceUplinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        },
        "deviceDownlinkThroughput": {
            "guaranteed": 0.0,
            "maximum": 0.0
        }
    }

    slice_response = {
        "slice": {
            "name": "slicefour",
            "notificationUrl": "",
            "notificationAuthToken": "samplenotificationtoken",
            "networkIdentifier": {
                "mcc": "236",
                "mnc": "30"
            },
            "sliceInfo": {
                "service_type": 1,
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "poligon": [
                {
                    "lat": 47.344,
                    "lon": 104.349
                },
                {
                    "lat": 35.344,
                    "lon": 76.619
                },
                {
                    "lat": 12.344,
                    "lon": 142.541
                },
                {
                    "lat": 19.43,
                    "lon": 103.53
                }
                ]
            },
            "maxDataConnections": 12,
            "maxDevices": 3,
            "sliceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "sliceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            }
            },
            "startPollingAt": 1691482014,
            "csi_id": "csi_989",
            "order_id": "6ed9b1b3-a6c5-49c2-8fa7-5cf70ba8fc23",
            "administrativeState": None,
            "state": "PENDING"
    }

    httpx_mock.add_response(
        method="PUT",
        match_content=to_bytes(slice_payload),
        json=slice_response,
        url="https://network-slicing.p-eu.rapidapi.com/slices"
    )

    """
b'{"networkIdentifier": {"mnc": "30", "mcc": "236"}, "sliceInfo": {"service_type": "eMBB", "differentiator": "AAABBB"}, "areaOfService": {"poligon": [{"longitude": 104.349, "latitude": 47.344}, {"longitude": 76.619, "latitude": 35.344}, {"longitude": 142.541, "latitude": 12.344}, {"longitude": 103.53, "latitude": 19.43}]}, "notificationUrl": "", "name": "slicefour", "notificationAuthToken": "samplenotificationtoken", "maxDataConnections": 12, "maxDevices": 3, "sliceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "sliceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}}' body amongst:
b'{"networkIdentifier": {"mnc": "30", "mcc": "236"}, "sliceInfo": {"service_type": "eMBB", "differentiator": "AAABBB"}, "areaOfService": {"poligon": [{"lat": 47.344, "lon": 104.349}, {"lat": 35.344, "lon": 76.619}, {"lat": 12.344, "lon": 142.541}, {"lat": 19.43, "lon": 103.53}]}, "notificationUrl": "", "name": "slicefour", "notificationAuthToken": "samplenotificationtoken", "maxDataConnections": 12, "maxDevices": 3, "sliceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "sliceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceUplinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}, "deviceDownlinkThroughput": {"guaranteed": 0.0, "maximum": 0.0}}' body
    """

    slice = client.slices.modify(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(poligon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )
    assert slice.name == slice_payload['name']
    assert slice.state == slice_response['state']

def test_get_all_slices(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    slices = [
        {
            "slice": {
            "name": "sliceone",
            "notificationUrl": "",
            "notificationAuthToken": "samplenotificationtoken",
            "networkIdentifier": {
                "mcc": "236",
                "mnc": "30"
            },
            "sliceInfo": {
                "service_type": 1,
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "poligon": [
                {
                    "lat": 47.344,
                    "lon": 104.349
                },
                {
                    "lat": 35.344,
                    "lon": 76.619
                },
                {
                    "lat": 12.344,
                    "lon": 142.541
                },
                {
                    "lat": 19.43,
                    "lon": 103.53
                }
                ]
            },
            "maxDataConnections": 12,
            "maxDevices": 3,
            "sliceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "sliceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceDownlinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            },
            "deviceUplinkThroughput": {
                "guaranteed": 0,
                "maximum": 0
            }
            },
            "startPollingAt": 1691482014,
            "csi_id": "csi_989",
            "order_id": "6ed9b1b3-a6c5-49c2-8fa7-5cf70ba8fc23",
            "administrativeState": None,
            "state": "inProgress"
        }
    ]

    
    httpx_mock.add_response(
        method="GET",
        url="https://network-slicing.p-eu.rapidapi.com/slices",
        json=slices
    )
    client.slices.getAll()

def test_get_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-slicing.p-eu.rapidapi.com/slices/{MOCK_SLICE['slice']['name']}"
    )
    
    response = client.slices.get(MOCK_SLICE['slice']['name'])
    assert response.sid == MOCK_SLICE['csi_id']

def test_activate_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        url="https://network-slicing.p-eu.rapidapi.com/slices/sliceone/activate"
    )

    assert client.slices.activate(slice_id="sliceone").status_code == 200

def test_deactivate_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        url="https://network-slicing.p-eu.rapidapi.com/slices/sliceone/deactivate"
    )

    assert client.slices.deactivate(slice_id="sliceone").status_code == 200

def test_delete_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="DELETE", 
        status_code=204,
        url="https://network-slicing.p-eu.rapidapi.com/slices/sliceone"
    )

    assert client.slices.delete(slice_id="sliceone").status_code == 204

def test_attach_device_to_slice(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-slicing.p-eu.rapidapi.com/slices/{MOCK_SLICE['slice']['name']}"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    httpx_mock.add_response(
        method="POST",
        url=f"https://device-attach-norc.p-eu.rapidapi.com/slice/{slice.name}/attach",
        json={
            "id": "string",
            "phoneNumber": "string",
            "deviceStatus": "ATTACHED",
            "progress": "INPROGRESS",
            "slice_id": "string"
        },
        match_content=to_bytes({
            "phoneNumber": "+12065550100",
            "notificationUrl": "https://notify.me/here"
        })
    )

    slice.attach(device, "https://notify.me/here")

def test_attach_device_to_slice_with_optional_params(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-slicing.p-eu.rapidapi.com/slices/{MOCK_SLICE['slice']['name']}"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    httpx_mock.add_response(
        method="POST",
        url=f"https://device-attach-norc.p-eu.rapidapi.com/slice/{slice.name}/attach",
        json={
            "id": "string",
            "phoneNumber": "string",
            "deviceStatus": "ATTACHED",
            "progress": "INPROGRESS",
            "slice_id": "string"
        },
        match_content=to_bytes({
            "phoneNumber": "+12065550100",
            "notificationUrl": "https://notify.me/here",
            "notificationAuthToken": "my_auth_token"
        })
    )

    slice.attach(device, "https://notify.me/here", notification_auth_token="my_auth_token")

def test_detach_device_from_slice(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-slicing.p-eu.rapidapi.com/slices/{MOCK_SLICE['slice']['name']}"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    httpx_mock.add_response(
        method="POST",
        url=f"https://device-attach-norc.p-eu.rapidapi.com/slice/{slice.name}/detach",
        json={
            "id": "string",
            "phoneNumber": "string",
            "deviceStatus": "ATTACHED",
            "progress": "INPROGRESS",
            "slice_id": "string"
        },
        match_content=to_bytes({
            "phoneNumber": "+12065550100",
            "notificationUrl": "https://notify.me/here"
        })
    )

    slice.detach(device, "https://notify.me/here")
