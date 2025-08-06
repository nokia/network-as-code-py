from network_as_code.models.device import Device
from network_as_code.errors import APIError

import pytest

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+367199991001")
    return device

@pytest.fixture
def forwarding_device(client) -> Device:
    device = client.devices.get(phone_number="+367199991000")
    return device


def test_device_is_unconditionally_call_forwarding(forwarding_device):

    assert forwarding_device.verify_unconditional_forwarding()

def test_device_is_not_unconditionally_forwarding(device):

    assert not device.verify_unconditional_forwarding()

def test_get_call_forwarding(forwarding_device):

    result = forwarding_device.get_call_forwarding()

    types = ['inactive', 'unconditional', 'conditional_busy', 'conditional_not_reachable', 'conditional_no_answer']

    assert isinstance(result, list)
    assert all([r in types for r in result])

def test_raise_error_with_empty_phone_number(client):
    device = client.devices.get(phone_number="")

    with pytest.raises(APIError):
        device.get_call_forwarding()
