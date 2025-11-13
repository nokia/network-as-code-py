import pytest
from datetime import datetime

from network_as_code.errors import AuthenticationException, NotFound, ServiceError, APIError


from network_as_code.models.device import Device, DeviceIpv4Addr

from network_as_code.models.device_status import AccessTokenCredential, EventType, PlainCredential

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("123456789@domain.com", phone_number="+123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")
    return device

@pytest.fixture
def device_with_just_public_ipv4_port(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", public_port=80))
    return device

@pytest.fixture
def device_with_just_phone_number(client) -> Device:
    device = client.devices.get(phone_number="7777777777")
    return device

def test_device_status_subscription_creation(httpx_mock, client, device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions",
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "initialEvent": True
            }
            }
        )

    subscription = client.device_status.subscribe(
        device=device,
        event_type=[EventType.REACHABILITY_DATA],
        subscription_expire_time="2024-07-17T13:18:23.682Z",
        sink="https://endpoint.example.com/sink",
        initial_event=True
    )

def test_device_status_subscription_creation_with_event_type_string_constant(httpx_mock, client, device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions",
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "initialEvent": True
            }
            }
        )

    subscription = client.device_status.subscribe(
        device=device,
        event_type=[EventType["REACHABILITY_SMS"]],
        subscription_expire_time="2024-07-17T13:18:23.682Z",
        sink="https://endpoint.example.com/sink",
        initial_event=True
    )

def test_subscribing_using_datetime(httpx_mock, client, device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions",
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-01-17T13:18:23.682000+00:00",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-01-17T13:18:23.682000+00:00",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            }
            }
        )

    subscription = client.device_status.subscribe(
        device=device,
        event_type=[EventType.REACHABILITY_SMS],
        subscription_expire_time=datetime.fromisoformat("2024-01-17T13:18:23.682+00:00"),
        sink="https://endpoint.example.com/sink",
        max_num_of_reports=5,
        initial_event=True
    )

def test_device_status_creation_minimal_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-01-17T13:18:23.682000+00:00",
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                }
            }
            }
    )

    subscription = client.device_status.subscribe(event_type=[EventType.REACHABILITY_SMS], sink="https://endpoint.example.com/sink", device=device)

def test_device_status_creation_minimal_parameters_minimal_ipv4_and_public_port(httpx_mock, device_with_just_public_ipv4_port, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "testuser@open5glab.net",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "publicPort": 80
                        },
                    }
                },
                "subscriptionExpireTime": "2024-01-17T13:18:23.682000+00:00",
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "protocol": "HTTP",
            "sink": "https://endpoint.example.com/sink",
            "types": ["org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "testuser@open5glab.net",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "publicPort": 80
                        }
                    }
                }
            }
        }
    )

    subscription = client.device_status.subscribe(event_type=["org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"], sink="https://endpoint.example.com/sink", device=device_with_just_public_ipv4_port)

def test_device_status_creation_minimal_parameters_only_phone_number(httpx_mock, device_with_just_phone_number, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "phoneNumber": "7777777777"
                    }
                },
                "subscriptionExpireTime": "2024-01-17T13:18:23.682000+00:00",
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "protocol": "HTTP",
            "sink": "https://endpoint.example.com/sink",
            "types": ["org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "phoneNumber": "7777777777"
                    },
                },
            }
        }
    )

    subscription = client.device_status.subscribe(event_type=[EventType['REACHABILITY_DATA']], sink="https://endpoint.example.com/sink", device=device_with_just_phone_number)

def test_device_status_creation_with_plain_credential(httpx_mock, device, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions",
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "sinkCredential": {
                "credentialType": "PLAIN",
                "identifier": "client-id",
                "secret": "client-secret"
            },
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-01-17T13:18:23.682000+00:00",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "sinkCredential": {
                "credentialType": "PLAIN",
                "identifier": "client-id",
                "secret": "client-secret"
            },
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            }
            }
    )
    
    subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_DATA],
        sink="https://endpoint.example.com/sink",
        device=device,
        sink_credential=PlainCredential(
            identifier = "client-id",
            secret =  "client-secret"
        ),
        subscription_expire_time="2024-07-17T13:18:23.682Z",
        max_num_of_reports=5,
        initial_event=True
        )
    
def test_device_status_creation_with_sink_credential_bearer(httpx_mock, device, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions",
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "sinkCredential":{
                "credentialType": "ACCESSTOKEN",
                "accessToken": "some-access-token",
                "accessTokenExpiresUtc": "2025-07-01T14:15:16.789Z",
                "accessTokenType": "bearer"
            },
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "sinkCredential":{
                "credentialType": "ACCESSTOKEN",
                "accessToken": "some-access-token",
                "accessTokenExpiresUtc": "2025-07-01T14:15:16.789Z",
                "accessTokenType": "bearer"
            },
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            }
            }
    )
    
    subscription = client.device_status.subscribe(
        event_type=[EventType.REACHABILITY_DATA],
        sink="https://endpoint.example.com/sink",
        device=device,
        sink_credential=AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc = "2025-07-01T14:15:16.789Z",
            access_token_type = "bearer"
        ),
        subscription_expire_time="2024-07-17T13:18:23.682Z",
        max_num_of_reports=5,
        initial_event=True,
        )


def test_device_status_roaming_subscription_creation(httpx_mock, client, device):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-roaming-status-subscriptions/v0.7/subscriptions",
        method="POST",
        json={
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "initialEvent": False
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },

        match_json={
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "initialEvent": False
            }
            }
        )

    subscription = client.device_status.subscribe(
        device=device,
        event_type=[EventType.ROAMING_ON],
        subscription_expire_time="2024-07-17T13:18:23.682Z",
        sink="https://endpoint.example.com/sink",
        initial_event=False
    )

def test_getting_device_reachability_subscription(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions/test-subscription",
        method="GET",
        json={
            "id": "test-subscription",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            }
    )
    
    subscription = client.device_status.get_reachability_subscription("test-subscription")

def test_getting_device_roaming_subscription(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-roaming-status-subscriptions/v0.7/subscriptions/test-subscription",
        method="GET",
        json={
            "id": "test-subscription",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            }
    )
    
    subscription = client.device_status.get_roaming_subscription("test-subscription")


def test_deleting_device_reachability_subscription(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions/test-subscription",
        method="GET",
        json={
            "id": "test-subscription",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            }
    )
    
    subscription = client.device_status.get_reachability_subscription("test-subscription")

    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions/test-subscription",
        method="DELETE",
    )

    subscription.delete()

def test_deleting_device_roaming_subscription(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-roaming-status-subscriptions/v0.7/subscriptions/test-subscription",
        method="GET",
        json={
            "id": "test-subscription",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            }
    )
    
    subscription = client.device_status.get_roaming_subscription("test-subscription")

    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-roaming-status-subscriptions/v0.7/subscriptions/test-subscription",
        method="DELETE",
    )

    subscription.delete()

def test_get_subscriptions(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-roaming-status-subscriptions/v0.7/subscriptions",
        method="GET",
        json=[{
            "id": "test-subscription",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },
            {
            "id": "test-subscription-2",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            }
            ]
    )
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status-subscriptions/v0.7/subscriptions",
        method="GET",
        json=[{
            "id": "test-subscription-3",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },
            {
            "id": "test-subscription-4",
            "sink": "https://endpoint.example.com/sink",
            "protocol": "HTTP",
            "types": [
                "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+123456789"
                }
                },
                "subscriptionExpireTime": "2024-07-17T13:18:23.682Z",
                "subscriptionMaxEvents": 5,
                "initialEvent": True
            },
            "startsAt": "2024-07-03T21:12:02.871Z",
            "expiresAt": "2024-07-03T21:12:02.871Z",
            "status": "ACTIVE"
            },
            ]
    )

    subscriptions = client.device_status.get_subscriptions()

    assert len(subscriptions) > 0

    for subscription in subscriptions:
        assert subscription.id
        assert subscription.device

def test_poll_reachability(httpx_mock, device):
    httpx_mock.add_response(
        method="POST",
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-reachability-status/v1/retrieve",
        json={
            "lastStatusTime": "2024-02-20T10:41:38.657Z",
            "reachable": True,
            "connectivity": [
                "SMS"
            ]
            },
        match_json={
            "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                }
        }
    )

    status = device.get_reachability()

    assert status.reachable
    assert status.connectivity == ["SMS"]

def test_poll_roaming(httpx_mock, device):
    httpx_mock.add_response(
        method="POST",
        url="https://network-as-code.p-eu.rapidapi.com/device-status/device-roaming-status/v1/retrieve",
        json={
            "lastStatusTime": "2024-02-20T10:41:38.657Z",
            "roaming": True,
            "countryCode": 358,
            "countryName": ["Finland"]
        },
        match_json={
            "device": {
                    "phoneNumber": "+123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
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
        client.device_status.subscribe(
            event_type="org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data",
            device=device, 
            max_num_of_reports=5, 
            sink="http://localhost:9090/notify"
        )

def test_subscribe_not_found(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=404
    )
    
    with pytest.raises(NotFound):
        client.device_status.subscribe(
            event_type="org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms",
            device=device,  
            max_num_of_reports=5, 
            sink="http://localhost:9090/notify"
        )

def test_subscribe_service_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=500
    )
    
    with pytest.raises(ServiceError):
        client.device_status.subscribe(
            event_type="org.camaraproject.device-reachability-status-subscriptions.v0.reachability-disconnected",
            device=device, 
            max_num_of_reports=5, 
            sink="http://localhost:9090/notify"
        )

def test_subscribe_api_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=400  
    )
    
    with pytest.raises(APIError):
        client.device_status.subscribe(
            event_type="org.camaraproject.device-roaming-status-subscriptions.v0.roaming-status",
            device=device, 
            max_num_of_reports=5, 
            sink="http://localhost:9090/notify"
        )
