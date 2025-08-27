import pytest
from datetime import datetime

from network_as_code.errors import AuthenticationException, NotFound, ServiceError, APIError


from network_as_code.models.device import Device, DeviceIpv4Addr

from network_as_code.models.device_status import EventType

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

@pytest.fixture
def device_with_just_public_ipv4_port(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))
    return device

@pytest.fixture
def device_with_just_phone_number(client) -> Device:
    device = client.devices.get(phone_number="7777777777")
    return device

def test_updated_device_status_subscription_creation(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions",
        method="POST",
        json={
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            },
            "subscriptionId": "qs15-h556-rt89-1298",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.connectivity.subscribe(
        device=device,
        event_type="org.camaraproject.device-status.v0.roaming-status",
        subscription_expire_time="2023-01-17T13:18:23.682Z",
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

def test_updated_device_status_subscription_creation_with_event_type_string_constant(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions",
        method="POST",
        json={
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.connectivity-data"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            },
            "subscriptionId": "qs15-h556-rt89-1298",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.connectivity-data"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.connectivity.subscribe(
        device=device,
        event_type=EventType.CONNECTIVITY_DATA,
        subscription_expire_time="2023-01-17T13:18:23.682Z",
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

def test_updated_device_status_subscription_creation_with_event_type_string_constant(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions",
        method="POST",
        json={
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            },
            "subscriptionId": "qs15-h556-rt89-1298",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.connectivity.subscribe(
        device=device,
        event_type=EventType["ROAMING_STATUS"],
        subscription_expire_time="2023-01-17T13:18:23.682Z",
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

def test_subscribing_using_datetime(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions",
        method="POST",
        json={
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682000+00:00",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            },
            "subscriptionId": "qs15-h556-rt89-1298",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682000+00:00",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.connectivity.subscribe(
        device=device,
        event_type="org.camaraproject.device-status.v0.roaming-status",
        subscription_expire_time=datetime.fromisoformat("2023-01-17T13:18:23.682+00:00"),
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

def test_device_status_creation_minimal_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "type": "org.camaraproject.device-status.v0.connectivity-data"
            },
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        }
    )

    subscription = client.connectivity.subscribe(event_type="org.camaraproject.device-status.v0.connectivity-data", notification_url="https://localhost:9090/notify", device=device, notification_auth_token="my_auth_token")

def test_device_status_creation_minimal_parameters_minimal_ipv4_and_public_port(httpx_mock, device_with_just_public_ipv4_port, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "publicPort": 80
                    }
                },
                "type": "org.camaraproject.device-status.v0.connectivity-sms"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        }
    )

    subscription = client.connectivity.subscribe(event_type="org.camaraproject.device-status.v0.connectivity-sms", notification_url="https://localhost:9090/notify", device=device_with_just_public_ipv4_port, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_device_status_creation_minimal_parameters_only_phone_number(httpx_mock, device_with_just_phone_number, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "7777777777"
                },
                "type": "org.camaraproject.device-status.v0.connectivity-data"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        }
    )

    subscription = client.connectivity.subscribe(event_type="org.camaraproject.device-status.v0.connectivity-data", notification_url="https://localhost:9090/notify", device=device_with_just_phone_number, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_device_status_creation_with_optional_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        json={
            "subscriptionId": "test-subscription",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "type": "org.camaraproject.device-status.v0.connectivity-sms"
            },
            "maxNumberOfReports": 1,
            "subscriptionExpireTime": "2023-08-31",
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        }
    )
    
    subscription = client.connectivity.subscribe(event_type="org.camaraproject.device-status.v0.connectivity-sms", notification_url="https://localhost:9090/notify", device=device, notification_auth_token="my_auth_token", subscription_expire_time="2023-08-31", max_num_of_reports=1)


def test_device_status_creation_with_roaming_status(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_json={
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        }
    )

    subscription = client.connectivity.subscribe(event_type="org.camaraproject.device-status.v0.roaming-status", notification_url="https://localhost:9090/notify", device=device, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_getting_device_status_subscription(httpx_mock, device, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions/test-subscription",
        method="GET",
        json={
            "subscriptionId": "test-subscription",
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Addresss": {
                        "publicAddress": "1.1.1.2",
                    },
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "http://localhost:9090/notify",
                "notificationAuthToken": "my-token"
            },
            "startsAt": "now",
        }
    )
    
    subscription = client.connectivity.get_subscription("test-subscription")


def test_deleting_device_status_subscription(httpx_mock, device, client):
    httpx_mock.add_response(
        method="GET",
        json={
            "subscriptionId": "test-subscription",
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Addresss": {
                        "publicAddress": "1.1.1.2"
                    },
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "http://localhost:9090/notify",
                "notificationAuthToken": "my-token"
            },
            "startsAt": "now",
        }
    )
    
    subscription = client.connectivity.get_subscription("test-subscription")

    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions/test-subscription",
        method="DELETE",
    )

    subscription.delete()

def test_get_subscriptions(httpx_mock, device, client):
    httpx_mock.add_response(
        method="GET",
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/subscriptions",
        json=[
            {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "testuser@testcsp.net"
                    },
                    "type": "org.camaraproject.device-status.v0.connectivity-data"
                },
                "maxNumberOfReports": 1,
                "webhook": {
                    "notificationUrl": "https://example.com"
                },
                "subscriptionId": "34e9e3ee-e281-4f47-bbc2-2431e6abbef0",
                "eventSubscriptionId": "34e9e3ee-e281-4f47-bbc2-2431e6abbef0",
                "startsAt": "2024-04-09T11:14:50.254312Z",
                "expiresAt": "2024-04-10T14:13:29.766268"
            },
            {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "testuser@testcsp.net"
                    },
                    "type": "org.camaraproject.device-status.v0.connectivity-data"
                },
                "maxNumberOfReports": 1,
                "webhook": {
                    "notificationUrl": "https://example.com"
                },
                "subscriptionId": "51b24d1a-26ae-4c9d-b114-2086da958c50",
                "eventSubscriptionId": "51b24d1a-26ae-4c9d-b114-2086da958c50",
                "startsAt": "2024-04-09T11:21:22.871187Z",
                "expiresAt": "2024-04-10T14:13:29Z"
            },
            {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "sdk-integration@testcsp.net",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "privateAddress": "1.1.1.2",
                            "publicPort": 80
                        }
                    },
                    "type": "org.camaraproject.device-status.v0.roaming-status",
                    "eventType": "ROAMING_STATUS"
                },
                "maxNumberOfReports": 1,
                "webhook": {
                    "notificationUrl": "http://192.0.2.0:8080/",
                    "notificationAuthToken": "c8974e592c2fa383d4a3960714"
                },
                "subscriptionId": "815e6da4-813d-4111-987d-5e6036aaa410",
                "eventSubscriptionId": "815e6da4-813d-4111-987d-5e6036aaa410",
                "startsAt": "2024-04-05T14:29:56.792078Z"
            },
            {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "sdk-integration@testcsp.net",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "privateAddress": "1.1.1.2",
                            "publicPort": 80
                        }
                    },
                    "type": "org.camaraproject.device-status.v0.connectivity-data"
                },
                "maxNumberOfReports": 1,
                "webhook": {
                    "notificationUrl": "http://192.0.2.0:8080/",
                    "notificationAuthToken": "c8974e592c2fa383d4a3960714"
                },
                "subscriptionId": "f6b03776-5e0f-4dbc-abce-30a916f94ad0",
                "eventSubscriptionId": "f6b03776-5e0f-4dbc-abce-30a916f94ad0",
                "startsAt": "2024-04-09T11:11:27.052869Z",
                "expiresAt": "2025-04-08T14:13:29.766268"
            }
        ]
    )

    subscriptions = client.connectivity.get_subscriptions()

    assert len(subscriptions) > 0

    for subscription in subscriptions:
        assert subscription.id
        assert subscription.device

def test_poll_connectivity(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/connectivity",
        json={
            "connectivityStatus": "CONNECTED_DATA"
        },
        match_json={
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            }
        }
    )

    status = device.get_connectivity()

    assert status == "CONNECTED_DATA"

def test_poll_roaming(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        url="https://network-as-code.p-eu.rapidapi.com/device-status/v0/roaming",
        json={
            "roaming": True,
            "countryCode": 358,
            "countryName": ["Finland"]
        },
        match_json={
            "device": {
                "networkAccessIdentifier": "testuser@open5glab.net",
                "ipv4Address": {
                    "publicAddress": "1.1.1.2",
                    "privateAddress": "1.1.1.2",
                    "publicPort": 80
                }
            }
        }
    )

    status = device.get_roaming()

    assert status.roaming
    assert status.country_code == 358
    assert status.country_name == ["Finland"]

def test_subscribe_authentication_exception(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=403
    )
    
    with pytest.raises(AuthenticationException):
        client.connectivity.subscribe(
            event_type="org.camaraproject.device-status.v0.connectivity-data",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="INVALID_TOKEN", 
        )

def test_subscribe_not_found(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=404
    )
    
    with pytest.raises(NotFound):
        client.connectivity.subscribe(
            event_type="org.camaraproject.device-status.v0.connectivity-sms",
            device=device,  
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="my-token"
        )

def test_subscribe_service_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=500
    )
    
    with pytest.raises(ServiceError):
        client.connectivity.subscribe(
            event_type="org.camaraproject.device-status.v0.connectivity_disconnected",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="my-token"
        )

def test_subscribe_api_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=400  
    )
    
    with pytest.raises(APIError):
        client.connectivity.subscribe(
            event_type="org.camaraproject.device-status.v0.connectivity-sms",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="my-token"
        )
