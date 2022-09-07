from requests import Response


class SubscriptionAPI:
    def get_subscription(self, id: str) -> dict:
        res = self._post("/subscriber", json={"sid": id})
        return self._result(res, json=True)

    def create_subscription(
        self,
        id: str,
        imsi: str,
        msisdn: str,
    ) -> dict:
        res: Response = self._put(
            "/admin/testuser",
            json={"sid": id, "imsi": imsi, "msisdn": msisdn},
        )
        return self._result(res, json=True)

    def delete_subscription(self, id: str, testmode: bool = True) -> bool:
        res: Response = self._delete(
            "/admin/testuser",
            json={"sid": id},
            headers={"x-testmode": "true" if testmode else "false"},
        )
        return True if res.status_code == 204 else False

    def get_subscriber_location(self, id: str) -> dict:
        res: Response = self._post("/subscriber/location", json={"sid": id})
        return self._result(res, json=True)

    def get_subscriber_bandwidth(self, id: str) -> dict:
        res: Response = self._post("/subscriber/bandwidth", json={"sid": id})
        return self._result(res, json=True)

    def set_subscriber_bandwidth(self, id: str, bandwidth: str) -> dict:
        res: Response = self._patch(
            "/subscriber/bandwidth",
            json={"sid": id, "bandwidth": bandwidth},
        )
        return self._result(res, json=True)

    def set_subscriber_custom_bandwidth(self, id: str, up: int, down: int) -> dict:
        res: Response = self._patch(
            "/subscriber/bandwidth/custom",
            json={"sid": id, "upload": up, "download": down},
        )
        return self._result(res, json=True)

    def get_subscriber_custom_bandwidth(self, id: str) -> dict:
        res: Response = self._patch("/subscriber/bandwidth/custom", json={"sid": id})
        return self._result(res, json=True)
