from httpx import Response


class SubscriptionAPI:
    def get_subscription(self, id: str) -> dict:
        res: Response = self.request("POST", "/subscriber", json={"sid": id})
        return self._result(res, json=True)

    def create_subscription(
        self,
        id: str,
        imsi: str,
        msisdn: str,
    ) -> dict:
        res: Response = self.request(
            "PUT",
            "/admin/testuser",
            json={"sid": id, "imsi": imsi, "msisdn": msisdn},
        )
        return self._result(res, json=True)

    def delete_subscription(self, id: str, testmode: bool = True) -> bool:
        res: Response = self.request(
            "DELETE",
            f"/admin/testuser/{id}",
            headers={"x-testmode": "true" if testmode else "false"},
        )
        return True if res.status_code == 204 else False

    def get_subscriber_location(self, id: str) -> dict:
        res: Response = self.request("POST", "/subscriber/location", json={"sid": id})
        return self._result(res, json=True)

    def get_subscriber_bandwidth(self, id: str) -> dict:
        res: Response = self.request("POST", "/subscriber/bandwidth", json={"sid": id})
        return self._result(res, json=True)

    def set_subscriber_bandwidth(self, id: str, bandwidth: str) -> dict:
        res: Response = self.request(
            "PATCH",
            "/subscriber/bandwidth",
            json={"sid": id, "bandwidth": bandwidth},
        )
        return self._result(res, json=True)

    def set_subscriber_custom_bandwidth(self, id: str, up: int, down: int) -> dict:
        res: Response = self.request(
            "PATCH",
            "/subscriber/bandwidth/custom",
            json={"sid": id, "upload": up, "download": down},
        )
        return self._result(res, json=True)

    def get_subscriber_custom_bandwidth(self, id: str) -> dict:
        res: Response = self.request(
            "PATCH", "/subscriber/bandwidth/custom", json={"sid": id}
        )
        return self._result(res, json=True)
