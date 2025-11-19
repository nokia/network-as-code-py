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
from pydantic import ConfigDict
from .kyc_match import CustomerMatch
from ..api.utils import to_camel

class FillInResult(CustomerMatch):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    phone_number: Optional[str] = None # type: ignore
    id_document_type: Optional[str] = None
    id_document_expiry_date: Optional[str] = None
    city_of_birth: Optional[str] = None
    country_of_birth: Optional[str] = None
    nationality: Optional[str] = None
