import json
from pytest_httpx import HTTPXMock
from network_as_code.client import NetworkAsCodeClient
from network_as_code.models.slice import NetworkIdentifier, Slice, SliceInfo, AreaOfService, Point, Throughput

def to_bytes(json_content: dict) -> bytes:
    return json.dumps(json_content).encode()


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

    slice = client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(poligon=[Point(lat=47.344, lon=104.349), Point(lat=35.344, lon=76.619), Point(lat=12.344, lon=142.541), Point(lat=19.43, lon=103.53)]),
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
    slice = {
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
    httpx_mock.add_response(
        method="GET",
        json=slice,
        url=f"https://network-slicing.p-eu.rapidapi.com/slices/{slice['slice']['name']}"
    )
    
    response = client.slices.get(slice['slice']['name'])
    assert response.sid == slice['csi_id']

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
        method="POST", 
        status_code=204,
        url="https://network-slicing.p-eu.rapidapi.com/slices/sliceone/delete"
    )

    assert client.slices.delete(slice_id="sliceone").status_code == 204