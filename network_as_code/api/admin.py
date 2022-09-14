class AdminAPI:
    def check_api_connection(self) -> str:
        """Used to determine if the API gateway and backend are accessible and working."""
        res = self.request("GET", "/admin/hello")
        return self._result(res, json=True)["service"]
