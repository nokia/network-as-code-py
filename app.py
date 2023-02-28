

import network_as_code as nac

def main():
    client = nac.NetworkAsCodeClient(token="<you-token-here>")

    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    session = device.create_session(service_ip="5.6.7.8", profile="M_L")

    device.clear_sessions()

main()
