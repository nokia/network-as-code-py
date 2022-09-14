from httpx import Response


class ServicesAPI:
    def get_all_services(self) -> list:
        res: Response = self.request("GET","/services")
        return self._result(res, json=True)

    def get_service(self, service_id: str) -> dict:
        res: Response = self.request("GET", f"/services/{service_id}")
        return self._result(res, json=True)

    def get_slice(self, service_id: str, slice_id: str) -> dict:
        """"""
        # TODO: Input validation
        res: Response = self.request("GET", f"/services/{service_id}/slices/{slice_id}")
        return self._result(res, json=True)

    def create_slice(
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
    ):
        # TODO: Input validation
        res: Response = self.request(
            "POST",
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
        return self._result(res, json=True)

    def delete_slice(self, service_id, slice_id) -> bool:
        res: Response = self.request("DELETE", f"/services/{service_id}/slices/{slice_id}")
        # TODO: Handle API errors with res.raise_for_status() since not using self._result()
        return res.status_code == 204
