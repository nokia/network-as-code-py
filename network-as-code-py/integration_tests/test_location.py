from network_as_code.client import NetworkAsCodeApi


class TestLocation:
    def test_retrieve_location(self, client: NetworkAsCodeApi):
        location = client.location.retrieve(
            device={"phone_number": "+36719991001"},
            max_age=60,
        )
        assert location is not None
        assert location.area is not None

    def test_verify_location_v0(self, client: NetworkAsCodeApi):
        result = client.location.verify(
            device={"phone_number": "+99999991000"},
            area={
                "area_type": "CIRCLE",
                "center": {"latitude": 47.48627616952785, "longitude": 19.07915612501993},
                "radius": 10000,
            },
        )
        assert result is not None
        assert result.verification_result is not None

    def test_verify_location_v1(self, client: NetworkAsCodeApi):
        result = client.location.verify_v1(
            device={"phone_number": "+99999991000"},
            area={
                "area_type": "CIRCLE",
                "center": {"latitude": 47.48627616952785, "longitude": 19.07915612501993},
                "radius": 10000,
            },
        )
        assert result is not None
        assert result.verification_result is not None
