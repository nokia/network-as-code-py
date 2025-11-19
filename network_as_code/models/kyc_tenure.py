
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

from datetime import datetime, date
from typing import Optional, Union
from pydantic import BaseModel, ConfigDict

from ..api.utils import to_camel

class TenureCheck(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)
    phone_number: str
    tenure_date: Union[str, datetime, date]

class TenureCheckResult(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, validate_by_alias=True)
    tenure_date_check: bool
    contract_type: Optional[str] = None
