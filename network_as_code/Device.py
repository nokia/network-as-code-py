from .RequestHandler import RequestHandler


class Device:
    def __init__(self, ext_id: str, sdk_token: str) -> None:
        self.ext_id = ext_id
        self.sdk_token = sdk_token

    def check_api_connection(self) -> bool:
        status = RequestHandler.instance.check_api_connection(self)
        return status == 200

    def location(self) -> dict:
        res = RequestHandler.instance.get_location(self)
        if res.status_code == 200:
            # location = res.json()
            # return location["longitude"], location["latitude"]
            return res.json()
        return {}
