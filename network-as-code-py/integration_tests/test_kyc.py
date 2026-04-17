import pytest

from network_as_code.client import NetworkAsCodeApi


class TestKycAgeVerification:
    def test_verify_age(self, client: NetworkAsCodeApi):
        result = client.kyc.verify_age(
            phone_number="+99999991000",
            age_threshold=18,
        )
        assert result is not None

    def test_verify_age_with_optional_params(self, client: NetworkAsCodeApi):
        result = client.kyc.verify_age(
            phone_number="+99999991000",
            age_threshold=18,
            id_document="66666666q",
            name="Federica Sanchez Arjona",
            given_name="Federica",
            family_name="Sanchez Arjona",
            middle_names="Sanchez",
            family_name_at_birth="YYYY",
            birthdate="1978-08-22",
            email="federicaSanchez.Arjona@example.com",
        )
        assert result is not None


class TestKycMatch:
    def test_match_customer(self, client: NetworkAsCodeApi):
        result = client.kyc.match(
            phone_number="+999999991000",
            id_document="66666666q",
            name="Federica Sanchez Arjona",
            given_name="Federica",
            family_name="Sanchez Arjona",
            middle_names="Sanchez",
            family_name_at_birth="YYYY",
            address="Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
            street_name="Nicolas Salmeron",
            street_number="4",
            postal_code="1028460",
            region="Tokyo",
            locality="ZZZZ",
            country="JP",
            house_number_extension="VVVV",
            birthdate="1978-08-22",
            email="abc@example.com",
            gender="OTHER",
        )
        assert result is not None
        assert result.id_document_match is not None

    def test_wrong_phone_number_returns_error(self, client: NetworkAsCodeApi):
        with pytest.raises(Exception):
            client.kyc.match(
                phone_number="+12345678",
                id_document="123456",
            )
