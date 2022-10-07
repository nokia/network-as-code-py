from typing import List
from network_as_code.models import Subscription
from network_as_code.namespaces import Namespace


class Subscriptions(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    async def get(self, id) -> Subscription:
        """Get a subscription by its external ID.

        Args:
            id (str): External ID of the subscription. Email-like.
        """
        res = await self.api.subscriptions.get_subscription(id)
        return Subscription(api=self.api, **res)

    async def create(
        self,
        id: str,
        imsi: str,
        msisdn: str,
    ) -> Subscription:
        """Create a new subscription. A subscription is typically tied to a mobile device.

        **Note!** At the moment it's only possible to create testmode subscriptions.

        Args:
            id (str): External ID of the subscription. Email-like.
            imsi (str): Phone-number like number with 14 to 16 digits.
            msisdn (str): Phone-number like number with 10 to 14 digits.

        Returns:
            A `Subscription` object.
        """
        data = await self.api.subscriptions.create_subscription(id, imsi, msisdn)
        return Subscription(**data)

    async def list(self) -> List[Subscription]:
        # TODO: Implement me!
        raise NotImplementedError
