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

from typing import Optional, Union
from pydantic import BaseModel, ConfigDict
from ..api.utils import to_camel

class KYCAge(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    age_threshold: int
    phone_number: Optional[str] = None
    id_document: Optional[str] = None
    name: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    middle_names: Optional[str] = None
    family_name_at_birth: Optional[str] = None
    birthdate: Optional[str] = None
    email: Optional[str] = None
    include_content_lock: Optional[bool] = None
    include_parental_control: Optional[bool] = None

class KYCAgeResult(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, validate_by_alias=True)
    age_check: str
    verified_status: Union[bool, str, None] = None
    identity_match_score: Optional[int] = None
    content_lock: Union[bool, str, None] = None
    parental_control: Union[bool, str, None] = None