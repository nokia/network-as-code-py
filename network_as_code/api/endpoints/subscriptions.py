from .endpoint import Endpoint, AsyncEndpoint


class SubscriptionsAPI(Endpoint):
    def get_subscription(self, id: str):
        res = self.client.request("POST", "/subscriber", json={"sid": id})
        return self.client._result(res, json=True)

    def create_subscription(
        self,
        id: str,
        imsi: str,
        msisdn: str,
    ):
        res = self.client.request(
            "PUT",
            "/admin/testuser",
            json={"sid": id, "imsi": imsi, "msisdn": msisdn},
        )
        return self.client._result(res, json=True)

    def delete_subscription(self, id: str, testmode: bool = True):
        res = self.client.request(
            "DELETE",
            f"/admin/testuser/{id}",
            headers={"x-testmode": "true" if testmode else "false"},
        )
        return True if res.status_code == 204 else False

    def get_subscriber_location(self, id: str):
        res = self.client.request("POST", "/subscriber/location", json={"sid": id})
        return self.client._result(res, json=True)

    def get_subscriber_bandwidth(self, id: str):
        res = self.client.request("POST", "/subscriber/bandwidth", json={"sid": id})
        return self.client._result(res, json=True)

    def set_subscriber_bandwidth(self, id: str, bandwidth: str):
        res = self.client.request(
            "PATCH",
            "/subscriber/bandwidth",
            json={"sid": id, "bandwidth": bandwidth},
        )
        return self.client._result(res, json=True)

    def set_subscriber_custom_bandwidth(self, id: str, up: int, down: int):
        res = self.client.request(
            "PATCH",
            "/subscriber/bandwidth/custom",
            json={"sid": id, "upload": up, "download": down},
        )
        return self.client._result(res, json=True)

    def get_subscriber_custom_bandwidth(self, id: str):
        res = self.client.request(
            "PATCH", "/subscriber/bandwidth/custom", json={"sid": id}
        )
        return self.client._result(res, json=True)
