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
            "X-RapidAPI-Host": rapid_host
        })

    def create_session(self, data: dict):
        """Function that hits the create session endpoint with the data

        Args:
            data (dict): _description_

        Returns:
            Session: response of the endpoint, ideally a Session
        """
        response = self.client.post(
            url= '/sessions',
            json=data
        )

        errors.error_handler(response)

        return response

    def get_all_sessions(self, device_id:dict) -> list:
        """This function retrieves all sessions given a device_id 

        Args:
            device_id (dict): The dict with device-id of the device whose sessions to retrieve

        Returns:
            list: returns list of session
        """
        response = self.client.get(
            url= f'/sessions?device-id={device_id.get("device-id")}'
        )

        errors.error_handler(response)

        return response

    def get_session(self, session_id:dict):
        """Returns a session given session ID

        Args:
            session_id (dict): A dict with a key session ID

        Returns:
            Session: the session object
        """
        response = self.client.get(
            url= f'/sessions/{session_id["sessionId"]}'
        )

        errors.error_handler(response)

        return response

    def delete_session(self, session_id:str):
        """Deletes a session given ID

        Args:
            session_id (str): session ID
        """
        response = self.client.delete(
            url= f'/sessions/{session_id}'
        )

        errors.error_handler(response)

        return response

