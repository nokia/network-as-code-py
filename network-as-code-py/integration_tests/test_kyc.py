import datetime
import pytest

from network_as_code.client import NetworkAsCodeApi


class TestKycFillIn:
    def test_fill_in_with_phone_number(self, client: NetworkAsCodeApi):
        result = client.kyc.fill_in(
            phone_number="+99999991000",
        )
        assert result is not None

    def test_fill_in_returns_identity_fields(self, client: NetworkAsCodeApi):
        result = client.kyc.fill_in(
            phone_number="+99999991000",
        )
        assert result is not None
        # All fields are optional — the operator populates what it has.
        # Verify that any returned fields have the expected types.
        if result.phone_number is not None:
            assert isinstance(result.phone_number, str)
        if result.name is not None:
            assert isinstance(result.name, str)
        if result.given_name is not None:
            assert isinstance(result.given_name, str)
        if result.family_name is not None:
            assert isinstance(result.family_name, str)
        if result.birthdate is not None:
            assert isinstance(result.birthdate, datetime.date)
        if result.email is not None:
            assert isinstance(result.email, str)
        if result.gender is not None:
            assert result.gender in ("MALE", "FEMALE", "OTHER")


class TestKycCheckTenure:
    def test_check_tenure_returns_boolean_result(self, client: NetworkAsCodeApi):
        result = client.kyc.check_tenure(
            phone_number="+99999991000",
            tenure_date=datetime.date(2023, 7, 3),
        )
        assert result is not None
        assert isinstance(result.tenure_date_check, bool)

    def test_check_tenure_contract_type_when_present(self, client: NetworkAsCodeApi):
        result = client.kyc.check_tenure(
            phone_number="+99999991000",
            tenure_date=datetime.date(2023, 7, 3),
        )
        assert result is not None
        if result.contract_type is not None:
            assert result.contract_type in ("PAYG", "PAYM", "Business")


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
