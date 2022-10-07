from typing import List
from network_as_code.api.endpoints import Endpoint


class ServicesAPI(Endpoint):
    async def get_all_services(self) -> List[dict]:
        res = await self.client.get("/services")
        return self.client.result(res, json=True)

    async def get_service(self, service_id: str) -> dict:
        res = await self.client.get(f"/services/{service_id}")
        return self.client.result(res, json=True)

    async def get_slice(self, service_id: str, slice_id: str) -> dict:
        res = await self.client.get(f"/services/{service_id}/slices/{slice_id}")
        return self.client.result(res, json=True)

    async def create_slice(
        self,
        service_id: str,
        slice_id: str,
        slice_name: str,
        slice_service_type: str,
        slice_differentiator: str,
        data_network_name: str,
        PLMN_name: str,
        region: str,
        set_id: str,
        access_point_name: str,
        packet_data_network_gateway: str,
    ) -> dict:
        # TODO: Input validation
        res = await self.client.post(
            f"/services/{service_id}/slices",
            json={
                "sliceTypeId": slice_id,
                "name": slice_name,
                "sst": slice_service_type,
                "sd": slice_differentiator,
                "listName": slice_name,
                "dnnList": data_network_name,
                "dataNetworkName": data_network_name,
                "plmnName": PLMN_name,
                "regionId": region,
                "setId": set_id,
                "apnName": access_point_name,
                "pdnGwId": packet_data_network_gateway,
            },
        )
        return self.client.result(res, json=True)

    async def delete_slice(self, service_id, slice_id) -> bool:
        res = await self.client.delete(f"/services/{service_id}/slices/{slice_id}")
        # TODO: Handle API errors with res.raise_for_status() since not using self.client.result()
        return res.status_code == 204
