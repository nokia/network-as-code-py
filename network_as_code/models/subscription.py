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
        res = self.client.api.get_subscription(id)
        return self.prepare_model(res)
