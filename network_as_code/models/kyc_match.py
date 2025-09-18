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

from typing import Optional
from pydantic import BaseModel, ConfigDict
from ..api.utils import to_camel

class KYCMatch(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    phone_number: Optional[str] = None
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

class KYCMatchResult(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, validate_by_alias=True)
    id_document_match: Optional[str] = None
    name_match: Optional[str] = None
    name_match_score: Optional[int] = None
    given_name_match: Optional[str] = None
    given_name_match_score: Optional[int] = None
    family_name_match: Optional[str] = None
    family_name_match_score: Optional[int] = None
    name_kana_hankaku_match: Optional[str] = None
    name_kana_hankaku_match_score: Optional[int] = None
    name_kana_zenkaku_match: Optional[str] = None
    name_kana_zenkaku_match_score: Optional[int] = None
    middle_names_match: Optional[str] = None
    middle_names_match_score: Optional[int] = None
    family_name_at_birth_match: Optional[str] = None
    family_name_at_birth_match_score: Optional[int] = None
    address_match: Optional[str] = None
    address_match_score: Optional[int] = None
    street_name_match: Optional[str] = None
    street_name_match_score: Optional[int] = None
    street_number_match: Optional[str] = None
    street_number_match_score: Optional[int] = None
    postal_code_match: Optional[str] = None
    region_match: Optional[str] = None
    region_match_score: Optional[int] = None
    locality_match: Optional[str] = None
    locality_match_score: Optional[int] = None
    country_match: Optional[str] = None
    house_number_extension_match: Optional[str] = None
    birthdate_match: Optional[str] = None
    email_match: Optional[str] = None
    email_match_score: Optional[int] = None
    gender_match: Optional[str] = None