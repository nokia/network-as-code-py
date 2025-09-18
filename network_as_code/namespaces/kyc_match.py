from typing import Optional
from . import Namespace
from ..models.verification import AccessToken
from ..models.kyc_match import CustomerMatch, CustomerMatchResult
from ..errors import InvalidParameter

class KYCMatch(Namespace):

    def match_customer(
            self,
            code: Optional[str] = None,
            phone_number: Optional[str] = None,
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
             match_customer parameters: A customers data that will be compared to data bound to their 
                                        phone number in the operator systems.
             code (string): The previously obtained authorization code. Can be used for authorization
                            independently or with phone_number
        #### Returns
             KYCMatchResult: Contains the result of matching the provided parameter values to the data 
                             in the operator system.
        """

        params = CustomerMatch(
            api=self.api,
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
        if code is None and phone_number is None:
            raise InvalidParameter("Either device phone number or authorization code is required.")

        if code:
            authenticator = AccessToken.create(self, code=code)
            headers = {'Authorization': f'{authenticator.token_type} {authenticator.access_token}'}
            match_params = self.api.kyc_match.match_customer(
                params.model_dump(by_alias=True, exclude_none=True),
                headers=headers
                )
        else:
            match_params = self.api.kyc_match.match_customer(params.model_dump(by_alias=True, exclude_none=True))
        
        return CustomerMatchResult.model_validate(match_params)