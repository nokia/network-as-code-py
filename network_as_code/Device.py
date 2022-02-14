
from .RequestHandler import RequestHandler

class Device:
    def __init__(self, imsi: str, sdk_token: str) -> None:
        self.imsi = imsi
        self.sdk_token = sdk_token

    def check_api_connection(self):
        res = RequestHandler.instance.check_api_connection(self)
        return res == 200
