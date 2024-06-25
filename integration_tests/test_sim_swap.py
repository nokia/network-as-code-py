
import pytest

from network_as_code.models.device import Device

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get(phone_number="3637123456")
    return device

def test_get_sim_swap_date(client, device):
    assert device.get_sim_swap_date()

def test_sim_swap_verify_without_max_age(client, device):
    assert device.verify_sim_swap()

def test_sim_swap_verify_with_max_age(client, device):
    assert device.verify_sim_swap(max_age=240)
