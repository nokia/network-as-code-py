import copy
import pytest
from typing import Any, Dict
from pytest_httpx import HTTPXMock
from network_as_code.client import NetworkAsCodeClient
from network_as_code.models.slice import Apps, NetworkIdentifier, Slice, SliceInfo, AreaOfService, Point, Throughput, TrafficCategories, Customer
from network_as_code.models.device import Device, DeviceIpv4Addr


from network_as_code.errors import InvalidParameter
from network_as_code.errors import AuthenticationException, NotFound, ServiceError, APIError

MOCK_SLICE: Dict[str, Any] = {
    "slice": {
            "name": "sliceone",
            "notificationUrl": "",
            "notificationAuthToken": "samplenotificationtoken",
            "networkIdentifier": {
                "mcc": "236",
                "mnc": "30"
            },
            "sliceInfo": {
                "serviceType": '1',
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "polygon": [
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
            "state": "PENDING"
}

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80), phone_number="+12065550100", imsi=1223334444)
    return device

def test_creating_a_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    slice_payload = {
        "networkIdentifier": {
            "mnc": "30",
            "mcc": "236"
        },
        "sliceInfo": {
            "serviceType": "eMBB",
            "differentiator": "AAABBB"
        },
        "notificationUrl": "https://example.com/notify",
        "name": "slicefour"
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
                "serviceType": 1,
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "polygon": [
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
        match_json=slice_payload,
        json=slice_response,
        url="https://network-as-code.p-eu.rapidapi.com/slice/v1/slices"
    )

    slice = client.slices.create(
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        notification_url="https://example.com/notify",
        name="slicefour",
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
                "serviceType": '1',
                "differentiator": "AAABBB"
            },
            "areaOfService": {
                "polygon": [
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
        url="https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }]
    )

    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/slice/v1/slices",
        json=slices
    )
    client.slices.get_all()
    

def test_get_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )
    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }]
    )
    
    response = client.slices.get(MOCK_SLICE['slice']['name'])
    assert response.sid == MOCK_SLICE['csi_id']

def test_get_slice_with_no_differentiator(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    MOCK_SLICE_RES: Dict[str, Any] = {
    "slice": {
            "name": "sliceone",
            "notificationUrl": "",
            "notificationAuthToken": "samplenotificationtoken",
            "networkIdentifier": {
                "mcc": "236",
                "mnc": "30"
            },
            "sliceInfo": {
                "serviceType": '1',
            },
            },
            "csi_id": "csi_368",
            "state": "PENDING"
}
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE_RES,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE_RES['slice']['name']}"
    )
    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json=[]
    )
    
    response = client.slices.get(MOCK_SLICE_RES['slice']['name'])

    assert response.sid == MOCK_SLICE_RES['csi_id']

def test_refresh_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )
    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }]
    )
    
    my_slice = client.slices.get(MOCK_SLICE['slice']['name'])

    assert my_slice.state == "PENDING"

    modified_slice = copy.deepcopy(MOCK_SLICE)
    modified_slice["state"] = "AVAILABLE"

    httpx_mock.add_response(
        method="GET",
        json=modified_slice,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    my_slice.refresh()

    assert my_slice.state == "AVAILABLE"

@pytest.mark.asyncio
async def test_slice_wait_for_polls_to_completion(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )
    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }]
    )
    
    my_slice = client.slices.get(MOCK_SLICE['slice']['name'])

    assert my_slice.state == "PENDING"

    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    modified_slice = copy.deepcopy(MOCK_SLICE)
    modified_slice["state"] = "AVAILABLE"

    httpx_mock.add_response(
        method="GET",
        json=modified_slice,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    await my_slice.wait_for()

    assert my_slice.state == "AVAILABLE"

@pytest.mark.asyncio
async def test_slice_wait_for_can_wait_for_arbitrary_state(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )
    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }]
    )
    
    my_slice = client.slices.get(MOCK_SLICE['slice']['name'])

    assert my_slice.state == "PENDING"

    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    modified_slice = copy.deepcopy(MOCK_SLICE)
    modified_slice["state"] = "AVAILABLE"

    httpx_mock.add_response(
        method="GET",
        json=modified_slice,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    await my_slice.wait_for()

    modified_slice = copy.deepcopy(MOCK_SLICE)
    modified_slice["state"] = "OPERATING"

    httpx_mock.add_response(
        method="GET",
        json=modified_slice,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    await my_slice.wait_for(desired_state="OPERATING")

    assert my_slice.state == "OPERATING"

def test_activate_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        url="https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/sliceone/activate"
    )
    slice = Slice(
            api=client._api,
            state = "NOT_SUBMITTED",
            name = "sliceone",
            network_identifier=NetworkIdentifier(mcc='236', mnc='30'),
            slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
            notification_url="https://example.com/notify"
    )
    slice.activate()

def test_deactivate_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        url="https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/sliceone/deactivate"
    )
    slice = Slice(
            api=client._api,
            state = "OPERATING",
            name = "sliceone",
            network_identifier=NetworkIdentifier(mcc='236', mnc='30'),
            slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
            notification_url="https://example.com/notify"
    )
    slice.deactivate()

def test_delete_slice(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="DELETE", 
        status_code=204,
        url="https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/sliceone"
    )
    slice = Slice(
            api=client._api,
            state = "DELETED",
            name = "sliceone",
            network_identifier=NetworkIdentifier(mcc='236', mnc='30'),
            slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
            notification_url="https://example.com/notify"
    )
    slice.delete()

def test_attach_device_to_slice_with_all_params(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100",
                    "imsi": 1223334444,
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    httpx_mock.add_response(
        method="POST",
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json={
            "nac_resource_id": "attachment-1"
        },
        match_json={
            "sliceId": "sliceone",
            "device": {
                "networkAccessIdentifier": device.network_access_identifier,
                "phoneNumber": device.phone_number,
                "ipv4Address": {
                    "publicAddress": device.ipv4_address.public_address,
                    "privateAddress": device.ipv4_address.private_address,
                    "publicPort": device.ipv4_address.public_port
                },
                "imsi": 1223334444,
            },
            "customer": {"name": "SDK_Customer"},
            "traffic_categories": {
                "apps": {
                    "os": "97a498e3-fc92-5c94-8986-0333d06e4e47",
                    "apps": ["ENTERPRISE"]
                }
            },
            "webhook": {
                "notificationUrl": "https://example.com/notifications",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            }
        }
    )

    slice.attach(device,customer=Customer(name="SDK_Customer"), traffic_categories=TrafficCategories(apps=Apps(
        os="97a498e3-fc92-5c94-8986-0333d06e4e47",
        apps=["ENTERPRISE"]
    )), notification_url="https://example.com/notifications",
    notification_auth_token="c8974e592c2fa383d4a3960714")

    
def test_attach_device_to_slice_with_only_manadatory_params(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "+12065550100"
                },
                "sliceId": "sliceone"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    httpx_mock.add_response(
        method="POST",
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments",
        json={
            "nac_resource_id": "attachment-1"
        },
        match_json={
            "sliceId": "sliceone",
            "device": {
                "phoneNumber": device.phone_number
            }
        }
    )

    device = client.devices.get(phone_number="+12065550100")
    slice.attach(device)    

def test_attach_device_to_slice_with_no_device_phone_number(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    device = client.devices.get("testuser@open5glab.net")
    with pytest.raises(InvalidParameter):
        slice.attach(device)



def test_detach_device_to_slice(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "+12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "+12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    httpx_mock.add_response(
        method="DELETE",
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments/attachment-1"
    )

    slice.detach(device)
    

def test_detach_device_from_slice_not_found(httpx_mock, client, device):
    httpx_mock.add_response(
        method="GET",
        json=MOCK_SLICE,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{MOCK_SLICE['slice']['name']}"
    )

    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )
    
    slice = client.slices.get(MOCK_SLICE['slice']['name'])

    # If the attachement id is not found in local storage, NotFound error will be thrown

    with pytest.raises(NotFound):
        slice.detach(device)

def test_get_atttachment(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json={
            "nac_resource_id":"4f11d02d-e661-4e4b-b623-55292a431c60"
        },
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments/4f11d02d-e661-4e4b-b623-55292a431c60"
    )
    
    response = client.slices.get_attachment("4f11d02d-e661-4e4b-b623-55292a431c60")
    assert response['nac_resource_id'] == "4f11d02d-e661-4e4b-b623-55292a431c60"

def test_get_all_atttachments(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )
    
    response = client.slices.get_all_attachments()
    assert len(response) == 3


def test_HTTPError_404_raises_NotFound(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        status_code=404
    )
    with pytest.raises(NotFound):
        client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )


def test_HTTPError_403_raises_AuthenticationException(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        status_code=403
    )
    with pytest.raises(AuthenticationException):
        client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )

def test_HTTPError_401_raises_AuthenticationException(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        status_code=401
    )
    with pytest.raises(AuthenticationException):
        client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )


def test_HTTPError_4XX_raises_APIError(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        status_code=400  # Can be any 4XX error code other than 401, 403, and 404.
    )
    with pytest.raises(APIError):
        client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )


def test_HTTPError_500_raises_ServiceError(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    httpx_mock.add_response(
        method="POST",
        status_code=500
    )
    with pytest.raises(ServiceError):
        client.slices.create(
        name="slicefour",
        network_id=NetworkIdentifier(mcc='236', mnc='30'),
        slice_info=SliceInfo(service_type='eMBB', differentiator='AAABBB'),
        area_of_service=AreaOfService(polygon=[Point(latitude=47.344, longitude=104.349), Point(latitude=35.344, longitude=76.619), Point(latitude=12.344, longitude=142.541), Point(latitude=19.43, longitude=103.53)]),
        notification_url="",
        notification_auth_token= "samplenotificationtoken",
        slice_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        slice_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        device_downlink_throughput=Throughput(guaranteed=0, maximum=0),
        device_uplink_throughput=Throughput(guaranteed=0, maximum=0),
        max_devices=3,
        max_data_connections=12
    )

def test_get_slice_missing_csi_id(httpx_mock: HTTPXMock, client: NetworkAsCodeClient):
    mock_slice_no_csi = MOCK_SLICE
    del mock_slice_no_csi['csi_id']
    httpx_mock.add_response(
        method="GET",
        json=mock_slice_no_csi,
        url=f"https://network-as-code.p-eu.rapidapi.com/slice/v1/slices/{mock_slice_no_csi['slice']['name']}"
    )

    httpx_mock.add_response(
        method="GET",
        json=[{
            "nac_resource_id": "attachment-1",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-2",
            "resource": {
                "device": {
                    "phoneNumber": "09213284343"
                },
                "sliceId": "sliceone"
            },
        }, {
            "nac_resource_id": "attachment-3",
            "resource": {
                "device": {
                    "phoneNumber": "12065550100"
                },
                "sliceId": "sdk-integration-slice-5"
            },
        }],
        url=f"https://network-as-code.p-eu.rapidapi.com/device-attach/v0/attachments"
    )

    response = client.slices.get(MOCK_SLICE['slice']['name'])
    assert response is not None
    assert response.sid is None
