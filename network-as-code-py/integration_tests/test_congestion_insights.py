from datetime import datetime, timedelta, timezone

from network_as_code.client import NetworkAsCodeApi


class TestCongestionInsights:
    def test_create_and_delete_subscription(self, client: NetworkAsCodeApi):
        expiration = (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat()

        subscription = client.congestion_insights.create_subscription(
            device={"phone_number": "+3670123456"},
            webhook={
                "notification_url": "https://example.com/notify",
                "notification_auth_token": "c8974e592c2fa383d4a3960714",
            },
            subscription_expire_time=expiration,
        )
        assert subscription is not None
        assert subscription.subscription_id is not None

        client.congestion_insights.delete_subscription(
            resource_id=subscription.subscription_id,
        )

    def test_get_subscription_by_id(self, client: NetworkAsCodeApi):
        expiration = (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat()

        subscription = client.congestion_insights.create_subscription(
            device={"phone_number": "+3670123456"},
            webhook={
                "notification_url": "https://example.com/notify",
                "notification_auth_token": "c8974e592c2fa383d4a3960714",
            },
            subscription_expire_time=expiration,
        )

        fetched = client.congestion_insights.get_subscription(
            resource_id=subscription.subscription_id,
        )
        assert fetched.subscription_id == subscription.subscription_id

        client.congestion_insights.delete_subscription(
            resource_id=subscription.subscription_id,
        )

    def test_list_subscriptions(self, client: NetworkAsCodeApi):
        subscriptions = client.congestion_insights.list_subscriptions()
        assert subscriptions is not None
        assert isinstance(subscriptions, list)

    def test_query_congestion(self, client: NetworkAsCodeApi):
        congestion = client.congestion_insights.query(
            device={"phone_number": "+99999991000"},
        )
        assert congestion is not None
        assert isinstance(congestion, list)
