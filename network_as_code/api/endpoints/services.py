from .endpoint import Endpoint, AsyncEndpoint


class ServicesAPI(Endpoint):
    def get_all_services(self):
        res = self.client.request("GET", "/services")
        return self.client._result(res, json=True)

    def get_service(self, service_id: str):
        res = self.client.request("GET", f"/services/{service_id}")
        return self.client._result(res, json=True)

    def get_slice(self, service_id: str, slice_id: str):
        """"""
        # TODO: Input validation
        res = self.client.request("GET", f"/services/{service_id}/slices/{slice_id}")
        return self.client._result(res, json=True)

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
        res = self.client.request(
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
        return self.client._result(res, json=True)

    def delete_slice(self, service_id, slice_id):
        res = self.client.request("DELETE", f"/services/{service_id}/slices/{slice_id}")
        # TODO: Handle API errors with res.raise_for_status() since not using self.client._result()
        return res.status_code == 204
