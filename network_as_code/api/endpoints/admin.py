from .endpoint import Endpoint, AsyncEndpoint


class AdminAPI(Endpoint):
    def check_api_connection(self):
        """Used to determine if the API gateway and backend are accessible and working."""
        res = self.client.request("GET", "/admin/hello")
        data = self.client._result(res, json=True)

        if isinstance(data, dict) and "service" in data:
            return data["service"]
        raise Exception(f"Endpoint '/admin/hello' did not return service information.")
