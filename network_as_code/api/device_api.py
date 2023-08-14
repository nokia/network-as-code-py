import httpx


class DeviceAPI:
    """
    Device API, that sends requests to the API via httpx calls
    """
    
    def __init__(self, host: str, key: str, url:str) -> None:
        """Methods takes host, key, and url. Then initialized the httpx client

        Args:
            host (str): RapidAPI Host
            key (str): RapidAPI Key
            url (str): URL for the httpx client
        """
        self.host = host
        self.key = key
        self.url = url
        self.client = httpx.Client(base_url=url)

    def create_session(self, data: dict):
        """Function that hits the create session endpoint with the data

        Args:
            data (dict): _description_

        Returns:
            Session: response of the endpoint, ideally a Session
        """
        print("-----------")
        print(data)
        response = self.client.post(
            url= '/sessions',
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': self.key,
                'X-RapidAPI-Host': self.host
            },
            json=data
        )

        response.raise_for_status()

        return response

    def get_all_sessions(self, device_id:dict) -> list:
        """This function retrieves all sessions given a device_id 

        Args:
            device_id (dict): The dict with device-id of the device whose sessions to retrieve

        Returns:
            list: returns list of session
        """
        response = self.client.get(
            url= f'/sessions?device-id={device_id.get("device-id")}',
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': self.key,
                'X-RapidAPI-Host': self.host
            }
        )

        response.raise_for_status()

        return response

    def get_session(self, session_id:dict):
        """Returns a session given session ID

        Args:
            session_id (dict): A dict with a key session ID

        Returns:
            Session: the session object
        """
        response = self.client.get(
            url= f'/sessions/{session_id["sessionId"]}',
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': self.key,
                'X-RapidAPI-Host': self.host
            }
        )

        response.raise_for_status()

        return response

    def delete_session(self, session_id:str):
        """Deletes a session given ID

        Args:
            session_id (str): session ID
        """
        response = self.client.delete(
            url= f'/sessions/{session_id}',
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': self.key,
                'X-RapidAPI-Host': self.host
            }
        )

        response.raise_for_status()

        return response
