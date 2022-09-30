from .endpoint import Endpoint


class AdminAPI(Endpoint):
    async def check_api_connection(self):
        """Used to determine if the API gateway and backend are accessible and working."""
        res = await self.client.get("/admin/hello")
        data = self.client._result(res, json=True)  # TODO: Data validation using Pydantic

        if isinstance(data, dict) and "service" in data:
            return data["service"]
        raise Exception("Endpoint 'GET /admin/hello' did not return service information.")
