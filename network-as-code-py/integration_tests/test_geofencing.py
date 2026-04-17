import pytest

from network_as_code.client import NetworkAsCodeApi


class TestGeofencing:
    def test_create_and_delete_subscription(self, client: NetworkAsCodeApi):
        subscription = client.geofencing.create_subscription(
            protocol="HTTP",
            sink="https://example.com/notify",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config={
                "subscription_detail": {
                    "device": {"phone_number": "+99999991000"},
                    "area": {"area_type": "CIRCLE"},
                },
                "initial_event": True,
            },
        )
        assert subscription is not None
        assert subscription.id is not None

        client.geofencing.delete_subscription(subscription_id=subscription.id)

    def test_get_subscription_by_id(self, client: NetworkAsCodeApi):
        subscription = client.geofencing.create_subscription(
            protocol="HTTP",
            sink="https://example.com/notify",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config={
                "subscription_detail": {
                    "device": {"phone_number": "+99999991000"},
                    "area": {"area_type": "CIRCLE"},
                },
            },
        )

        fetched = client.geofencing.get_subscription(subscription_id=subscription.id)
        assert fetched.id == subscription.id

        client.geofencing.delete_subscription(subscription_id=subscription.id)

    def test_list_subscriptions(self, client: NetworkAsCodeApi):
        subscriptions = client.geofencing.list_subscriptions()
        assert subscriptions is not None
        assert isinstance(subscriptions, list)

    def test_fail_to_get_deleted_subscription(self, client: NetworkAsCodeApi):
        subscription = client.geofencing.create_subscription(
            protocol="HTTP",
            sink="https://example.com/notify",
            types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
            config={
                "subscription_detail": {
                    "device": {"phone_number": "+99999991000"},
                    "area": {"area_type": "CIRCLE"},
                },
            },
        )

        client.geofencing.delete_subscription(subscription_id=subscription.id)

        with pytest.raises(Exception):
            client.geofencing.get_subscription(subscription_id=subscription.id)
