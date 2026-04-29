from network_as_code.client import NetworkAsCodeApi


class TestDeviceStatus:
    def test_poll_roaming_status(self, client: NetworkAsCodeApi):
        status = client.device_status.retrieve_roaming_status(
            device={"phone_number": "+99999991000"},
        )
        assert status is not None
        assert status.roaming is not None

    def test_poll_reachability_status(self, client: NetworkAsCodeApi):
        status = client.device_status.retrieve_reachability_status(
            device={"phone_number": "+99999991000"},
        )
        assert status is not None
        assert status.reachable is not None

    def test_check_connectivity(self, client: NetworkAsCodeApi):
        status = client.device_status.check_connectivity(
            device={"phone_number": "+99999991000"},
        )
        assert status is not None
        assert status.connectivity_status is not None

    def test_check_roaming_v0(self, client: NetworkAsCodeApi):
        status = client.device_status.check_roaming(
            device={"phone_number": "+99999991000"},
        )
        assert status is not None
        assert status.roaming is not None

    def test_create_and_delete_roaming_subscription(self, client: NetworkAsCodeApi):
        subscription = client.device_status.create_roaming_subscription(
            protocol="HTTP",
            sink="https://example.com/notify",
            types=["org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"],
            config={
                "subscription_detail": {"device": {"phone_number": "+99999991000"}},
                "initial_event": True,
            },
        )
        assert subscription.id is not None

        client.device_status.delete_roaming_subscription(subscription_id=subscription.id)

    def test_create_and_delete_reachability_subscription(self, client: NetworkAsCodeApi):
        subscription = client.device_status.create_reachability_subscription(
            protocol="HTTP",
            sink="https://example.com/notify",
            types=["org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data"],
            config={
                "subscription_detail": {"device": {"phone_number": "+99999991000"}},
                "initial_event": True,
            },
        )
        assert subscription.id is not None

        client.device_status.delete_reachability_subscription(subscription_id=subscription.id)

    def test_get_roaming_subscription_by_id(self, client: NetworkAsCodeApi):
        subscription = client.device_status.create_roaming_subscription(
            protocol="HTTP",
            sink="https://example.com/notify",
            types=["org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on"],
            config={
                "subscription_detail": {"device": {"phone_number": "+99999991000"}},
                "initial_event": True,
            },
        )

        fetched = client.device_status.get_roaming_subscription(subscription_id=subscription.id)
        assert fetched.id == subscription.id

        client.device_status.delete_roaming_subscription(subscription_id=subscription.id)

    def test_list_subscriptions(self, client: NetworkAsCodeApi):
        subscriptions = client.device_status.list_subscriptions()
        assert subscriptions is not None
        assert isinstance(subscriptions, list)
