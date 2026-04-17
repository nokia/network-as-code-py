from network_as_code.client import NetworkAsCodeApi


class TestCallForwarding:
    def test_check_unconditional_call_forwarding(self, client: NetworkAsCodeApi):
        result = client.call_forwarding_signal.retrieve_unconditional_call_forwarding(
            phone_number="+99999991111",
        )
        assert result is not None
        assert result.active is not None

    def test_retrieve_call_forwarding_services(self, client: NetworkAsCodeApi):
        result = client.call_forwarding_signal.retrieve_call_forwarding(
            phone_number="+999999991111",
        )
        assert result is not None
        assert isinstance(result, list)
