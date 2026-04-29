import datetime
import pytest

from network_as_code.client import NetworkAsCodeApi


class TestNumberRecycling:
    def test_check_returns_boolean_result(self, client: NetworkAsCodeApi):
        result = client.number_recycling.check(
            phone_number="+99999991000",
            specified_date=datetime.date(2024, 10, 31),
        )
        assert result is not None
        assert isinstance(result.phone_number_recycled, bool)

    def test_check_recycled_true(self, client: NetworkAsCodeApi):
        # A date well in the past should indicate the number has been recycled
        result = client.number_recycling.check(
            phone_number="+99999991000",
            specified_date=datetime.date(2020, 1, 1),
        )
        assert result.phone_number_recycled is True

    def test_check_recycled_false(self, client: NetworkAsCodeApi):
        # A very recent date should indicate no recycling has occurred
        result = client.number_recycling.check(
            phone_number="+99999991001",
            specified_date=datetime.date(2020, 1, 1),
        )
        assert result.phone_number_recycled is False

    def test_check_invalid_phone_number_raises_error(self, client: NetworkAsCodeApi):
        with pytest.raises(Exception):
            client.number_recycling.check(
                phone_number="+12345678",
                specified_date=datetime.date(2024, 10, 31),
            )
