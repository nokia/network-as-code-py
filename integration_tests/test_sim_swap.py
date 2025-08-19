
from datetime import datetime

import pytest

from network_as_code.models.device import Device

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="+99999991000")
    return device

def test_get_sim_swap_date(device):
    assert type(device.get_sim_swap_date()) is datetime

def test_sim_swap_verify_without_max_age(device):
    assert device.verify_sim_swap()

def test_sim_swap_verify_with_max_age(device):
    assert device.verify_sim_swap(max_age=240)

def test_sim_swap_verify_true(client):
    device = client.devices.get(phone_number="+99999991000")

    assert device.verify_sim_swap()

def test_sim_swap_verify_false(client):
    device = client.devices.get(phone_number="+99999991001")

    assert not device.verify_sim_swap()