# Copyright 2023 Nokia
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
from datetime import datetime
from pydantic import BaseModel

class VerificationResult(BaseModel):
    """
    A class representing the `Location verification result` model.

    #### Public Attributes:
            result_type (str): the `result_type` of a VerificationResult object.
            match_rate (int): the `match_rate` in case of result_type is "Partial" of a VerificationResult object.
            last_location_time (datetime): the `last_location_time` of the VerificationResult object.
    """
    result_type: str
    match_rate: Optional[int] = None
    last_location_time: Optional[datetime] = None

class Location(BaseModel):
    """
    A class representing the `Location` model.

    #### Public Attributes:
            longitude (float): the `longitude` of a location object.
            latitude (float): the `latitude` of a location object.
            radius (Optional[float]): the `radius` of a location object.
    """

    longitude: float
    latitude: float
    radius: Optional[float] = None
