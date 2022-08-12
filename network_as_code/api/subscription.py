from requests import Response


class SubscriptionAPI:
    def get_subscription(self, id: str) -> dict:
        res = self._post("/subscriber", json={"id": id})
        return self._result(res, json=True)

    def create_subscription(
        self,
        id: str,
        imsi: str,
        msisdn: str,
        testmode: bool = True,
    ) -> dict:
        res: Response = self._put(
            "/subscriber/testuser",
            json={"id": id, "imsi": imsi, "msisdn": msisdn},
            headers={"x-testmode": "true" if testmode else "false"},
        )
        assert res.status_code == 201  # Check for correct status code
        return self._result(res, json=True)

    def delete_subscription(self, id: str, testmode: bool = True) -> bool:
        res: Response = self._delete(
            "/subscriber/testuser",
            json={"id": id},
            headers={"x-testmode": "true" if testmode else "false"},
        )
        return True if res.status_code == 204 else False

    def get_subscriber_location(self, id: str) -> dict:
        res: Response = self._post("/subscriber/location", json={"id": id})
        return self._result(res, json=True)

    def get_subscriber_bandwidth(self, id: str) -> dict:
        res: Response = self._post("/subscriber/bandwidth", json={"id": id})
        return self._result(res, json=True)

    def set_subscriber_bandwidth(self, id: str, bandwidth: str) -> dict:
        res: Response = self._patch(
            "/subscriber/bandwidth",
            json={"id": id, "bandwidth": bandwidth},
        )
        return self._result(res, json=True)
