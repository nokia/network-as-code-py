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

from pydantic import BaseModel
from typing import Optional


class CivicAddress(BaseModel):
    country: Optional[str]
    a1: Optional[str]
    a2: Optional[str]
    a3: Optional[str]
    a4: Optional[str]
    a5: Optional[str]
    a6: Optional[str]


class Location(BaseModel):
    """
    A class representing the `Location` model.

    #### Public Attributes:
            longitude (float): the `longitude` of a location object.
            latitude (float): the `latitude` of a location object.
            civic_address (Optional[CivicAddress]): the `civic_address` of a location object.
    """

    longitude: float
    latitude: float
    civic_address: Optional[CivicAddress]
