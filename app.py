

import network_as_code as nac
from network_as_code.client import NetworkAsCodeClient

def main():
    device = client.devices.get("my_device@nokia.com", ip = "10.0.12.35")

    session = device.create_session(service_ip="10.0.23.20", service_tier="QOS_L")

    execute_bandwidth_intensive_task()

    device.clear_sessions()

