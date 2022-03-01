
from .RequestHandler import RequestHandler

class Device:
    def __init__(self, ext_id: str, sdk_token: str) -> None:
        self.ext_id = ext_id
        self.sdk_token = sdk_token

    def check_api_connection(self):
        res = RequestHandler.instance.check_api_connection(self)
        return res == 200
