# Copyright 2025 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Optional, Union
from pydantic import BaseModel, ConfigDict, PrivateAttr, model_validator

from ..api import APIClient
from ..api.utils import to_camel, str_to_bool

class CustomerMatch(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    _api: APIClient = PrivateAttr()
    phone_number: str
    id_document: Optional[str] = None
    name: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    name_kana_hankaku: Optional[str] = None
    name_kana_zenkaku: Optional[str] = None
    middle_names: Optional[str] = None
    family_name_at_birth: Optional[str] = None
    address: Optional[str] = None
    street_name: Optional[str] = None
    street_number: Optional[str] = None
    postal_code: Optional[str] = None
    region: Optional[str] = None
    locality: Optional[str] = None
    country: Optional[str] = None
    house_number_extension: Optional[str] = None
    birthdate: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None

    def __init__(self, api: APIClient, **data) -> None:
        super().__init__(**data)
        self._api = api

class CustomerMatchResult(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, validate_by_alias=True)
    id_document_match: Union[bool, str, None] = None
    name_match: Union[bool, str, None] = None
    name_match_score: Optional[int] = None
    given_name_match: Union[bool, str, None] = None
    given_name_match_score: Optional[int] = None
    family_name_match: Union[bool, str, None] = None
    family_name_match_score: Optional[int] = None
    name_kana_hankaku_match: Union[bool, str, None] = None
    name_kana_hankaku_match_score: Optional[int] = None
    name_kana_zenkaku_match: Union[bool, str, None] = None
    name_kana_zenkaku_match_score: Optional[int] = None
    middle_names_match: Union[bool, str, None] = None
    middle_names_match_score: Optional[int] = None
    family_name_at_birth_match: Union[bool, str, None] = None
    family_name_at_birth_match_score: Optional[int] = None
    address_match: Union[bool, str, None] = None
    address_match_score: Optional[int] = None
    street_name_match: Union[bool, str, None] = None
    street_name_match_score: Optional[int] = None
    street_number_match: Union[bool, str, None] = None
    street_number_match_score: Optional[int] = None
    postal_code_match: Union[bool, str, None] = None
    region_match: Union[bool, str, None] = None
    region_match_score: Optional[int] = None
    locality_match: Union[bool, str, None] = None
    locality_match_score: Optional[int] = None
    country_match: Union[bool, str, None] = None
    house_number_extension_match: Union[bool, str, None] = None
    birthdate_match: Union[bool, str, None] = None
    email_match: Union[bool, str, None] = None
    email_match_score: Optional[int] = None
    gender_match: Union[bool, str, None] = None

    @model_validator(mode='before')
    @classmethod
    def compile_params(cls, data: Any) -> Any:
        if isinstance(data, dict):
            return {k: str_to_bool(v) for k, v in data.items()}
        return data