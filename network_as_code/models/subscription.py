from pydantic import BaseModel, EmailStr, PrivateAttr
from ..models import Location, Bandwidth, CustomBandwidth
from ..api import APIClient


class Subscription(BaseModel):
    api: APIClient = PrivateAttr()
    sid: EmailStr
    imsi: str
    msisdn: str

    async def location(self) -> Location:
        data = await self.api.subscriptions.get_subscriber_location(self.sid)
        location_info_field = "locationInfo"
        if location_info_field not in data:
            raise RuntimeError(f"API did not return {location_info_field}")
        return Location(**data[location_info_field])


    async def get_bandwidth(self):
        """Query the current bandwidth profile of the subscriber.

        Returns:
            Either a `Bandwidth` or `CustomBandwidth` depending on the type of current profile.
        """
        data = await self.api.subscriptions.get_subscriber_bandwidth(self.sid)

        if "serviceTier" in data and data["serviceTier"] == "custom":
            data = await self.api.subscriptions.get_subscriber_custom_bandwidth(self.sid)
            return CustomBandwidth(**data)
        return Bandwidth(**data)

    async def set_bandwidth(self, *, name: str = None, up: int = None, down: int = None):
        """Modify bandwidth profile of the subscription.

        This function accepts either a predefined bandwidth profile `name` or a custom set of parameters.
        Keep in mind that the custom bandwidth configuration will be provided as "best effort".

        Args:
            name (str): Name of a predefined bandwidth profile
            up: (int): Desired custom upload speed in bits per second
            down (int): Desired custom download speed in bits per second

        Returns:
            `Bandwidth` if a `name` was given, or `CustomBandwidth` if custom values were given.
        """
        if name is not None and (up is not None or down is not None):
            raise RuntimeError("Can't set the bandwidth 'name' and 'up/down' simultaneuosly.")

        if name:
            data = await self.api.subscriptions.set_subscriber_bandwidth(self.sid, name)
            return Bandwidth(**data)

        elif up > 0 and down > 0:
            data = await self.api.subscriptions.set_subscriber_custom_bandwidth(self.sid, up, down)
            return CustomBandwidth(**data)

    async def delete(self):
        """Delete a subscription. A subscription is typically tied to a device.

        #### Note! Only a test-mode subscription can be deleted!
        """
        # TODO: Add a way to check whether this subscription is real or simulated.
        return await self.api.subscriptions.delete_subscription(self.sid)
