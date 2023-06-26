from os import access
from pydantic import BaseModel, EmailStr, PrivateAttr
from typing import List, Union

from qos_client.model.create_session import CreateSession
from qos_client.model.ports_spec import PortsSpec
from qos_client.schemas import unset

from ..api import APIClient
from ..models.session import Session
from ..models.location import CivicAddress, Location
from ..errors import DeviceNotFound, NotFound, error_handler

class Device(BaseModel):
    """
    A class representing the `Device` model.

    #### Private Attributes:
        _api(APIClient): An API client object.
        _sessions(List[Session]): List of device session instances.


    #### Public Attributes:
        sid(EmailStr): Device Identifier email string.
        ip(str): IP address of the device.

    #### Public Methods:
        create_session (Session): Creates a session for the device.
        sessions (List[Session]): Returns all the sessions created by the device id.
        clear_sessions (): Deletes all the sessions created by the device id.
        location (Location): Gets the location of the device and returns a Location client object.
        verify_location (bool): Verifies if a device is located in a given location point.
    """

    _api: APIClient = PrivateAttr()
    _sessions: List[Session] = PrivateAttr()
    sid: EmailStr
    ip: str 

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api
        self._sessions = []

    @property
    def id(self):
        return str(self.sid)

    def create_session(self, service_ip, profile, device_ports: Union[None, PortsSpec] = None, service_ports: Union[None, PortsSpec] = None, duration = None, notification_url = None):
        """Creates a session for the device.

        #### Args:
            service_ip (any): IP address of the service.
            profile (any): Name of the requested QoS profile.
            device_ports (optional): List of the device ports.
            service_ports (optional): List of the application server ports.
            duration (optional): Session duration in seconds.
            notification_url (optional): Notification URL for session-related events.

        #### Example:
            ```python
            session = device.create_session(service_ip="5.6.7.8", profile="QOS_L", notification_url="https://example.com/notifications")
            ```
        """
        session_resource = {
            "qosProfile": profile,
            "id": self.sid,
            "ip": self.ip,
            "devicePorts": device_ports.dict(by_alias=True) if device_ports is not None else unset,
            "appIp": service_ip,
            "applicationServerPorts": service_ports.dict(by_alias=True) if service_ports is not None else unset,
        }

        if duration:
            session_resource["duration"] = duration

        if notification_url:
            session_resource["notificationUrl"] = notification_url


        # Error Case: Creating session
        global session 
        session = error_handler(func=self._api.sessions.create_session, arg=session_resource)
        # session = self._api.sessions.create_session(session_resource)
        session = session.body

        return Session.convert_session_model(self._api, self.ip, session)

    def sessions(self) -> List[Session]:
        """List sessions of the device.

        #### Example:
            ```python
            sessions = device.sessions()
            ```
        """
        # Error Case: Getting all sessions
        sessions = error_handler(func=self._api.sessions.get_all_sessions, arg={"device-id": self.sid})
        # sessions = self._api.sessions.get_all_sessions(query_params={"device-id": self.sid})
        if not sessions:
            return []
        else:
            return list(map(lambda session : self.__convert_session_model(session), sessions.body))

    def clear_sessions(self):
        """Clears sessions of the device."""
        for session in self.sessions():
            session.delete()

    def __convert_session_model(self, session) -> Session:
       return Session.convert_session_model(self._api, self.ip, session)

    def location(self) -> Location:
        """Returns the location of the device.

        #### Example:
            ```python
            location = device.location()
            ```
        """
        query_parameters = {
           "device_id": self.sid 
        }

        # Error Case: Getting location
        global response
        response = error_handler(func=self._api.location.get_location, arg=query_parameters)
        # response = self._api.location.get_location(query_parameters)
        body = response.body

        longitude = body["point"]["lon"]
        latitude = body["point"]["lat"]
        civic_address = None

        if "civicAddress" in body.keys():
            civic_address = CivicAddress(
                country=body["civicAddress"]["country"],
                a1=body["civicAddress"]["A1"] if isinstance(body["civicAddress"]["A1"], str) else None,
                a2=body["civicAddress"]["A2"] if isinstance(body["civicAddress"]["A2"], str) else None,
                a3=body["civicAddress"]["A3"] if isinstance(body["civicAddress"]["A3"], str) else None,
                a4=body["civicAddress"]["A4"] if isinstance(body["civicAddress"]["A4"], str) else None,
                a5=body["civicAddress"]["A5"] if isinstance(body["civicAddress"]["A5"], str) else None,
                a6=body["civicAddress"]["A6"] if isinstance(body["civicAddress"]["A6"], str) else None
            )

        return Location(longitude=longitude, latitude=latitude, civic_address=civic_address)

    def verify_location(self, longitude: float, latitude: float, accuracy: str) -> bool:
        """Verifies the location of the device(Returns boolean value).

        #### Args:
            longitude (float): longitude of the device.
            latitude (float): longitude of the device.
            accuracy (str): Accuracy range in distance.
            
        #### Example:
            ```python
            located? = device.verify_location(longitude=24.07915612501993, latitude=47.48627616952785, accuracy="10km")
            ```
        """
        query_parameters = {
            "device_id": self.sid,
            "longitude": longitude,
            "latitude": latitude,
            "accuracy": accuracy
        }

        try:
            # Error Case: Verifying location
            global res
            res = error_handler(func=self._api.location.verify_location, arg=query_parameters)
            return res.body
            # return self._api.location.verify_location(query_parameters).body
        except:
            return False
