from datetime import datetime

import pytest

from network_as_code.models.device import Device

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+99999991001")
    return device

def test_get_device_swap_date(device):
    assert type(device.get_device_swap_date()) is datetime

def test_device_swap_verify_without_max_age(device):
    assert device.verify_device_swap()

def test_device_swap_verify_with_max_age(device):
    assert device.verify_device_swap(max_age=240)

def test_device_swap_verify_true(device):
    assert device.verify_device_swap()

def test_device_swap_verify_false(device):
    assert not device.verify_device_swap(max_age=1)