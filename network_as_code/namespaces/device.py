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

from typing import Union
from . import Namespace
from ..models import Device, DeviceIpv4Addr


class Devices(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    def get(
        self,
        network_access_identifier: Union[None, str] = None,
        ipv4_address: Union[None, DeviceIpv4Addr]= None,
        ipv6_address=None,
        phone_number=None,
        imsi=None,
    ) -> Device:
        """Get a subscription by its external ID.

        Args:
            network_access_identifier (str): External ID of the subscription. Email-like.
            ipv4_address (DeviceIpv4Addr | None): ipv4 address of the subscription.
            ipv6_address (Any | None): ipv6 address of the subscription.
            phone_number (Any | None): phone number of the subscription.
            imsi (Any | None): International mobile subscriber identity.

        #### Example:
             '''python
             device = client.devices.get("testuser@testcsp.net", 
             ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", 
             private_address="1.1.1.2", public_port=80), 
             phone_number="+3670123456", imsi=1223334444)
             '''    
        Returns: Device
        """

        assert any(
            [id, ipv4_address, ipv6_address, phone_number]
        ), "At least one parameter must be set."

        # If the user only supplied a public IPv4 address without a public address or port, let's assume the
        # device is not NAT'd and we can just rely on one IP
        if ipv4_address and (ipv4_address.public_address
                             and (not ipv4_address.private_address and not ipv4_address.public_port)):
            ipv4_address.private_address = ipv4_address.public_address

        ret_device = Device(
            api=self.api,
            network_access_identifier=network_access_identifier,
            ipv4_address=ipv4_address,
            ipv6_address=ipv6_address,
            phone_number=phone_number,
            imsi=imsi,
        )
        return ret_device
