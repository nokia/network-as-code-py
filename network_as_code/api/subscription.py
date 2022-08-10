class SubscriptionAPI:
    def get_subscription(self, external_id: str):
        res = self._post("/subscriber", json={"id": external_id})
        return self._result(res, json=True)
