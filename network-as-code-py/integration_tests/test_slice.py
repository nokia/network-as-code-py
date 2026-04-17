import random

from network_as_code.client import NetworkAsCodeApi


class TestSlice:
    def test_create_and_delete_slice(self, client: NetworkAsCodeApi):
        rand = random.randint(1, 1000)
        result = client.slice.create_slice(
            network_identifier={"mcc": "236", "mnc": "30"},
            slice_info={"service_type": "eMBB", "differentiator": "444444"},
            notification_url="https://notify.me/here",
            name=f"slice{rand}",
            notification_auth_token="my-token",
        )
        assert result is not None
        assert result.csi_id is not None

        client.slice.delete_slice(id=result.name)

    def test_create_slice_with_optional_args(self, client: NetworkAsCodeApi):
        rand = random.randint(1, 1000)
        result = client.slice.create_slice(
            network_identifier={"mcc": "236", "mnc": "30"},
            slice_info={"service_type": "eMBB", "differentiator": "444444"},
            notification_url="https://notify.me/here",
            name=f"slice{rand}",
            notification_auth_token="my-token",
            area_of_service={
                "polygon": [
                    {"lat": 47.344, "lon": 104.349},
                    {"lat": 35.344, "lon": 76.619},
                    {"lat": 12.344, "lon": 142.541},
                    {"lat": 19.43, "lon": 103.53},
                ],
            },
            slice_downlink_throughput={"guaranteed": 3415, "maximum": 1234324},
            slice_uplink_throughput={"guaranteed": 3415, "maximum": 1234324},
            device_uplink_throughput={"guaranteed": 3415, "maximum": 1234324},
            device_downlink_throughput={"guaranteed": 3415, "maximum": 1234324},
            max_data_connections=10,
            max_devices=5,
        )
        assert result is not None

        client.slice.delete_slice(id=result.name)

    def test_get_slice_by_name(self, client: NetworkAsCodeApi):
        rand = random.randint(1, 1000)
        name = f"slice{rand}"

        created = client.slice.create_slice(
            network_identifier={"mcc": "236", "mnc": "30"},
            slice_info={"service_type": "eMBB", "differentiator": "444444"},
            notification_url="https://notify.me/here",
            name=name,
            notification_auth_token="my-token",
        )

        fetched = client.slice.get_slice(id=created.name)
        assert fetched is not None

        client.slice.delete_slice(id=created.name)

    def test_list_slices(self, client: NetworkAsCodeApi):
        slices = client.slice.list_slices()
        assert slices is not None
        assert isinstance(slices, list)
