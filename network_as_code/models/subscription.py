from .resource import Model, Collection


class Subscription(Model):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.

    Args:
        id (str): External ID of the subscription. Follows email address conventions.
    """

    @property
    def imsi(self):
        return self.attrs.get("imsi")

    @property
    def msisdn(self):
        return self.attrs.get("msisdn")

    def get_location(self) -> dict:
        res = self.client.api.get_subscriber_location(self.id)
        return res.get("locationInfo")

    def get_bandwidth(self) -> str:
        res = self.client.api.get_subscriber_bandwidth(self.id)
        return res.get("bandwidth")

    def set_bandwidth(self) -> str:
        res = self.client.api.set_subscriber_bandwidth(self.id)
        return res.get("bandwidth")


class SubscriptionCollection(Collection):
    model = Subscription

    def get(self, id):
        """Get a subscription by its external ID.

        Args:
            id (str): External ID of the subscription.

        Returns:
            A :py:class:`Subscription` object.

        Raises:
            :py:class:`network_as_code.errors.NotFound`
                If the subscription does not exist.
            :py:class:`network_as_code.errors.APIError`
                If the server returns an error.
        """
        # TODO: Value checking here.
        res = self.client.api.get_subscription(id)
        return self.prepare_model(res)

    def list(self):
        # TODO: Implement me!
        raise NotImplementedError

    def create(self, id: str, imsi: str, msisdn: str, testmode: bool = True):
        """Create a new subscription. A subscription is typically tied to a device.

        #### Note! At the moment it's only possible to create testmode subscriptions.

        Args:
            id (str): External ID of the subscription. Email-like.
            imsi (str): Phone-number like number with 14 to 16 digits.
            msisdn (str): Phone-number like number with 10 to 14 digits.
            testmode (bool): Whether to create a simulated or real subscription.

        Returns:
            A :py:class:`Subscription` object.

        Raises:
            :py:class:`network_as_code.errors.NotFound`
                If the subscription does not exist.
            :py:class:`network_as_code.errors.APIError`
                If the server returns an error.
        """
        # TODO: Value checking here.
        res = self.client.api.create_subscription(id, imsi, msisdn, testmode)
        return self.prepare_model(res)
