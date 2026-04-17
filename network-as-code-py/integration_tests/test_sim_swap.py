from network_as_code.client import NetworkAsCodeApi


class TestSimSwap:
    def test_retrieve_sim_swap_date(self, client: NetworkAsCodeApi):
        response = client.sim_swap.retrieve_date(phone_number="+99999991000")
        assert response is not None
        assert response.latest_sim_change is not None

    def test_check_sim_swap_without_max_age(self, client: NetworkAsCodeApi):
        response = client.sim_swap.check(phone_number="+99999991000")
        assert response is not None
        assert response.swapped is True

    def test_check_sim_swap_with_max_age(self, client: NetworkAsCodeApi):
        response = client.sim_swap.check(phone_number="+99999991000", max_age=120)
        assert response.swapped is True

    def test_check_sim_swap_true(self, client: NetworkAsCodeApi):
        response = client.sim_swap.check(phone_number="+99999991000", max_age=120)
        assert response.swapped is True

    def test_check_sim_swap_false(self, client: NetworkAsCodeApi):
        response = client.sim_swap.check(phone_number="+99999991001", max_age=120)
        assert response.swapped is False
