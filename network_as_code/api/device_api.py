from typing import Union
import httpx


from .. import errors


class DeviceAPI:
    """
    Device API, that sends requests to the API via httpx calls
    """

    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        """Methods takes rapid_host, rapid_key, and base_url. Then initialized the httpx client

        Args:
            rapid_host (str): RapidAPI Host
            rapid_key (str): RapidAPI Key
            base_url (str): URL for the httpx client
        """
        self.client = httpx.Client(
            base_url=base_url,
            headers={
                "content-type": "application/json",
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": rapid_host,
            },
        )

    def create_session(
        self,
        sid,
        ipv4_address,
        phone_number,
        profile,
        service_ipv4,
        service_ipv6=None,
        device_ports: Union[None, any] = None,
        service_ports: Union[None, any] = None,
        duration=None,
        notification_url=None,
        notification_auth_token=None,
    ):
        """Function that hits the create session endpoint with the data

        #### Args:
            profile (any): Name of the requested QoS profile.
            service_ipv4 (any): IPv4 address of the service.
            service_ipv6 (optional): IPv6 address of the service.
            device_ports (optional): List of the device ports.
            service_ports (optional): List of the application server ports.
            duration (optional): Session duration in seconds.
            notification_url (optional): Notification URL for session-related events.
            notification_token (optional): Security bearer token to authenticate registration of session.

        Returns:
            Session: response of the endpoint, ideally a Session
        """

        session_resource = {
            "qosProfile": profile,
            "device": {"ipv4Address": {}},
            "applicationServer": {"ipv4Address": service_ipv4},
            "devicePorts": device_ports.dict(by_alias=True)
            if device_ports is not None
            else None,
            "applicationServerPorts": service_ports.dict(by_alias=True)
            if service_ports is not None
            else None,
        }

        if sid:
            session_resource["device"]["networkAccessIdentifier"] = sid

        if ipv4_address:
            if ipv4_address.public_address:
                session_resource["device"]["ipv4Address"][
                    "publicAddress"
                ] = ipv4_address.public_address
            if ipv4_address.private_address:
                session_resource["device"]["ipv4Address"][
                    "privateAddress"
                ] = ipv4_address.private_address
            if ipv4_address.public_port:
                session_resource["device"]["ipv4Address"][
                    "publicPort"
                ] = ipv4_address.public_port

        if phone_number:
            session_resource["device"]["phoneNumber"] = phone_number

        if service_ipv6:
            session_resource["applicationServer"]["ipv6Address"] = service_ipv6

        if duration:
            session_resource["duration"] = duration

        if notification_url:
            session_resource["notificationUrl"] = notification_url

        if notification_auth_token:
            session_resource["notificationAuthToken"] = (
                "Bearer " + notification_auth_token
            )

        response = self.client.post(url="/sessions", json=session_resource)

        errors.error_handler(response)

        return response

    def get_all_sessions(self, device) -> list:
        """This function retrieves all sessions given a device_id

        Args:
            device_id (dict): The dict with device-id of the device whose sessions to retrieve

        Returns:
            list: returns list of session
        """
        url = ""

        if device.network_access_identifier:
            url = (
                f"/sessions?networkAccessIdentifier={device.network_access_identifier}"
            )
        elif device.phone_number:
            url = f"/sessions?phoneNumber={device.phone_number}"

        response = self.client.get(url=url)

        errors.error_handler(response)

        return response

    def get_session(self, sessionId: str):
        """Returns a session given session ID

        Args:
            sessionId (str): A string session ID

        Returns:
            Session: the session object
        """
        response = self.client.get(url=f"/sessions/{sessionId}")

        errors.error_handler(response)

        return response

    def delete_session(self, id: str):
        """Deletes a session given session ID

        Args:
            id (str): session ID
        """
        response = self.client.delete(url=f"/sessions/{id}")

        errors.error_handler(response)

        return response
