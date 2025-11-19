from typing import Optional, Union
from datetime import datetime, date
from . import Namespace
from ..models.kyc_match import CustomerMatch, CustomerMatchResult
from ..models.kyc_age import AgeVerification, AgeVerificationResult
from ..models.kyc_tenure import TenureCheck, TenureCheckResult
from ..models.kyc_fill import FillInResult

class KYC(Namespace):

    def match_customer(
            self,
            phone_number: str,
            id_document: Optional[str] = None,
            name: Optional[str] = None,
            given_name: Optional[str] = None,
            family_name: Optional[str] = None,
            name_kana_hankaku: Optional[str] = None,
            name_kana_zenkaku: Optional[str] = None,
            middle_names: Optional[str] = None,
            family_name_at_birth: Optional[str] = None,
            address: Optional[str] = None,
            street_name: Optional[str] = None,
            street_number: Optional[str] = None,
            postal_code: Optional[str] = None,
            region: Optional[str] = None,
            locality: Optional[str] = None,
            country: Optional[str] = None,
            house_number_extension: Optional[str] = None,
            birthdate: Optional[str] = None,
            email: Optional[str] = None,
            gender: Optional[str] = None,
            ) -> CustomerMatchResult:
        """Match a customer identity against the account data bound to their phone number.
        #### Args
             phone_number (str): Used as an identifier for the request.
             match_customer parameters: A customers data that will be compared to data bound to their 
                                        phone number in the operator systems.
        #### Returns
             KYCMatchResult: Contains the result of matching the provided parameter values to the data 
                             in the operator system.
        """

        params = CustomerMatch(
            phone_number = phone_number,
            id_document = id_document,
            name = name,
            given_name = given_name,
            family_name = family_name,
            name_kana_hankaku = name_kana_hankaku,
            name_kana_zenkaku = name_kana_zenkaku,
            middle_names = middle_names,
            family_name_at_birth = family_name_at_birth,
            address = address,
            street_name = street_name,
            street_number = street_number,
            postal_code = postal_code,
            region = region,
            locality = locality,
            country = country,
            house_number_extension = house_number_extension,
            birthdate = birthdate,
            email = email,
            gender = gender
        )
        match_params = self.api.kyc_match.match_customer(params.model_dump(by_alias=True, exclude_none=True))

        return CustomerMatchResult.model_validate(self.__parse_string_params(match_params))

    def verify_age(
            self,
            age_threshold: int,
            phone_number: str,
            id_document: Optional[str] = None,
            name: Optional[str] = None,
            given_name: Optional[str] = None,
            family_name: Optional[str] = None,
            middle_names: Optional[str] = None,
            family_name_at_birth: Optional[str] = None,
            birthdate: Optional[str] = None,
            email: Optional[str] = None,
            include_content_lock: Optional[bool] = None,
            include_parental_control: Optional[bool] = None,
            ) -> AgeVerificationResult:
        """Checks if the age of the subscriber is older than the age threshold in the request.
        #### Args
             age_threshold (int): The age threshold from which the age of the user must be compared
             phone_number (str): Used as an identifier for the request.
             additional verify_age parameters: E.g. name, birthdate, include_parental_control. 
                                               Confirms that the subscriber is the contract's 
                                               owner or if the subscription has any kind of parental 
                                               or content control activated.
        #### Returns
             KYCAgeResult: Object containing the result of age threshold check and verification 
                           status. Might also hold information about parental or content control 
                           status and score result of additional checks.
        """
        params = AgeVerification(
            age_threshold = age_threshold,
            phone_number = phone_number,
            id_document = id_document,
            name = name,
            given_name = given_name,
            family_name = family_name,
            middle_names = middle_names,
            family_name_at_birth = family_name_at_birth,
            birthdate = birthdate,
            email = email,
            include_content_lock = include_content_lock,
            include_parental_control = include_parental_control
        )
        match_params = self.api.kyc_age.verify_age(params.model_dump(by_alias=True, exclude_none=True))

        return AgeVerificationResult.model_validate(self.__parse_string_params(match_params))

    def check_tenure(
        self,
        phone_number: str,
        tenure_date: Union[str, datetime, date]
    ) -> TenureCheckResult:
        """Check if the network subscriber has been a customer of the service provider for the specified amount of time.
        #### Args
             phone_number (str): Used as an identifier for the request.
             tenure_date (Union[str, datetime, date]): The specified minimum tenure date from which the 
             continuous tenure is to be confirmed.
        #### Returns
             TenureCheckResult: Object containing boolean value for the tenure date 
                                check and optional contract type, if known.
        """

        tenure_date = (
            tenure_date.date().isoformat()
            if isinstance(tenure_date, datetime)
            else tenure_date.isoformat() if isinstance(tenure_date, date)
            else tenure_date
        )
        params = TenureCheck(
            phone_number = phone_number,
            tenure_date = tenure_date
        )
        match_params = self.api.kyc_tenure.check_tenure(params.model_dump(by_alias=True))

        return TenureCheckResult.model_validate(match_params)


    def request_customer_info(self, phone_number: str) -> FillInResult:
        """Request customer information against the account data bound to their phone number.
        #### Args
             phone_number (str): Used as an identifier for the request.
        #### Returns
             FillInResult: Contains the user information available on file by the user's Operator KYC records.
        """
        fill_params = self.api.kyc_fill.request_customer_info(phone_number)

        return FillInResult.model_validate(self.__parse_string_params(fill_params))

    def __parse_string_params(self, params: dict) -> dict:
        for k, v in params.items():
            if v in ["not_available", "unknown"]:
                params[k] = None

        return params
