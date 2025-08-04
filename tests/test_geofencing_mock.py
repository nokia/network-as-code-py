import pytest

from network_as_code.models.device import DeviceIpv4Addr, Device
from network_as_code.models.geofencing import PlainCredential, AccessTokenCredential, EventType
from network_as_code.errors import NotFound, AuthenticationException, APIError, ServiceError



@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

def test_creating_geofencing_subscription_area_entered_type(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions",
        method="POST",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-entered"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "publicPort": 80
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
        },
        match_json=
        {
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-entered"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "publicPort": 80
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="+123456789", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        subscription_expire_time="2025-01-23T10:40:30.616Z",
        subscription_max_events=1,
        initial_event=False
    )

    assert subscription.event_subscription_id

def test_creating_geofencing_subscription_area_entered_event_type(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions",
        method="POST",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-entered"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "publicPort": 80
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
        },
        match_json=
        {
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-entered"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "1.1.1.2",
                            "publicPort": 80
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="+123456789", ipv4_address=DeviceIpv4Addr(public_address="1.1.1.2", public_port=80), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=[EventType["AREA_ENTERED"]],
        latitude=-90,
        longitude=-180,
        radius=2001,
        subscription_expire_time="2025-01-23T10:40:30.616Z",
        subscription_max_events=1,
        initial_event=False
    )

    assert subscription.event_subscription_id


def test_creating_geofencing_subscription_area_left_type(httpx_mock,device, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions",
        method="POST",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "+123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
            },
        match_json=
        {
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "84.125.93.10",
                            "publicPort": 59765
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="+123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=[EventType.AREA_LEFT],
        latitude=-90,
        longitude=-180,
        radius=2001,
        subscription_expire_time="2025-01-23T10:40:30.616Z",
        subscription_max_events=1,
        initial_event=False
    )

def test_creating_geofencing_subscription_sink_credential_plain(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions",
        method= "POST",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "sinkCredential": {
                "credentialType": "PLAIN",
                "identifier": "client-id",
                "secret": "client-secret"
            },
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "+123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
            },
        match_json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "84.125.93.10",
                            "publicPort": 59765
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "sinkCredential": {
                "credentialType": "PLAIN",
                "identifier": "client-id",
                "secret": "client-secret"
            }
        }
    )

    device = client.devices.get("123456789@domain.com", phone_number="+123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")
    
    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        sink_credential=PlainCredential(
                identifier = "client-id",
                secret =  "client-secret"
        ),
        subscription_expire_time="2025-01-23T10:40:30.616Z",
        subscription_max_events=1,
        initial_event=False
    )

def test_creating_geofencing_subscription_sink_credential_bearer(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions",
        method= "POST",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "sinkCredential":{
                "credentialType": "ACCESSTOKEN",
                "accessToken": "some-access-token",
                "accessTokenExpiresUtc": "2025-07-01T14:15:16.789Z",
                "accessTokenType": "bearer"
            },
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "123456789@domain.com",
                    "phoneNumber": "+123456789",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
            },
        match_json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
            ],
            "config": {
                "subscriptionDetail": {
                    "device": {
                        "networkAccessIdentifier": "123456789@domain.com",
                        "phoneNumber": "+123456789",
                        "ipv4Address": {
                            "publicAddress": "84.125.93.10",
                            "publicPort": 59765
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "area": {
                        "areaType": "CIRCLE",
                        "center": {
                            "latitude": -90,
                            "longitude": -180
                        },
                        "radius": 2001
                    }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "sinkCredential":{
                "credentialType": "ACCESSTOKEN",
                "accessToken": "some-access-token",
                "accessTokenExpiresUtc": "2025-07-01T14:15:16.789Z",
                "accessTokenType": "bearer"
            },
        }
    )
    device = client.devices.get("123456789@domain.com", phone_number="+123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.geofencing.subscribe(
        device=device,
        sink="https://example.com/",
        types=["org.camaraproject.geofencing-subscriptions.v0.area-left"],
        latitude=-90,
        longitude=-180,
        radius=2001,
        sink_credential= AccessTokenCredential(
            access_token= "some-access-token",
            access_token_expires_utc = "2025-07-01T14:15:16.789Z",
            access_token_type = "bearer"
        ),
        subscription_expire_time="2025-01-23T10:40:30.616Z",
        subscription_max_events=1,
        initial_event=False
    )


def test_getting_geofencing_subscription(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions/de87e438-58b4-42c3-9d49-0fbfbd878305",
        method="GET",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "sinkCredential": {},
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
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
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
            }
    )
    subscription = client.geofencing.get("de87e438-58b4-42c3-9d49-0fbfbd878305")

def test_getting_geofencing_subscriptions(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions",
        method="GET",
        json=[
            {
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "sinkCredential": {},
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
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
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
            },
            {
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "sinkCredential": {},
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-entered"
            ],
            "config": {
                "subscriptionDetail": {
                "device": {
                    "phoneNumber": "+987654321",
                    "networkAccessIdentifier": "987654321@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 3200
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:30:30.616Z"
            }
        ]
    )
    subscriptions = client.geofencing.get_all()

    assert len(subscriptions) > 0

    for subscription in subscriptions:
        assert subscription.event_subscription_id
        
    

def test_deleting_geofencing_subscription(httpx_mock, client):
    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions/de87e438-58b4-42c3-9d49-0fbfbd878305",
        method="GET",
        json={
            "protocol": "HTTP",
            "sink": "https://example.com/",
            "sinkCredential": {},
            "types": [
                "org.camaraproject.geofencing-subscriptions.v0.area-left"
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
                },
                "area": {
                    "areaType": "CIRCLE",
                    "center": {
                    "latitude": -90,
                    "longitude": -180
                    },
                    "radius": 2001
                }
                },
                "subscriptionExpireTime": "2025-01-23T10:40:30.616Z",
                "subscriptionMaxEvents": 1,
                "initialEvent": False
            },
            "id": "de87e438-58b4-42c3-9d49-0fbfbd878305",
            "startsAt": "2025-01-23T10:40:30.616Z"
            }
    )
    subscription = client.geofencing.get("de87e438-58b4-42c3-9d49-0fbfbd878305")

    httpx_mock.add_response(
        url="https://network-as-code.p-eu.rapidapi.com/geofencing-subscriptions/v0.3/subscriptions/de87e438-58b4-42c3-9d49-0fbfbd878305",
        method="DELETE",
    )
    subscription.delete()

def test_subscribe_authentication_exception(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=403
    )
    
    with pytest.raises(AuthenticationException):
        client.geofencing.subscribe(
            device=device,
            sink="https://example.com/",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            latitude=-90,
            longitude=-180,
            radius=2001,
            subscription_expire_time="2025-01-23T10:40:30.616Z",
            subscription_max_events=1,
            initial_event=False
        )

def test_subscribe_not_found(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=404
    )
    
    with pytest.raises(NotFound):
        client.geofencing.subscribe(
            device=device,
            sink="https://example.com/",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            latitude=-90,
            longitude=-180,
            radius=2001,
            subscription_expire_time="2025-01-23T10:40:30.616Z",
            subscription_max_events=1,
            initial_event=False
        )

def test_subscribe_service_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=500
    )
    
    with pytest.raises(ServiceError):
        client.geofencing.subscribe(
            device=device,
            sink="https://example.com/",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            latitude=-90,
            longitude=-180,
            radius=2001,
            subscription_expire_time="2025-01-23T10:40:30.616Z",
            subscription_max_events=1,
            initial_event=False
        )

def test_subscribe_api_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=400  
    )
    
    with pytest.raises(APIError):
        client.geofencing.subscribe(
            device=device,
            sink="https://example.com/",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            latitude=-90,
            longitude=-180,
            radius=2001,
            subscription_expire_time="2025-01-23T10:40:30.616Z",
            subscription_max_events=1,
            initial_event=False
        )
