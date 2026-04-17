import pytest

from network_as_code.client import NetworkAsCodeApi


class TestQoD:
    def test_create_and_delete_session_v1(self, client: NetworkAsCodeApi):
        session = client.qod.create_session_v_1(
            device={
                "phone_number": "+99999991001",
                "ipv4Address": {
                    "publicAddress": "233.252.0.2",
                    "privateAddress": "233.252.0.2"
                },
            },
            application_server={"ipv_4_address": "8.8.8.8"},
            qos_profile="DOWNLINK_M_UPLINK_L",
            duration=60,
        )
        assert session is not None
        assert session.session_id is not None

        client.qod.delete_session_v_1(session_id=session.session_id)

    def test_get_session_by_id(self, client: NetworkAsCodeApi):
        session = client.qod.create_session_v_1(
            device={
                "network_access_identifier": "testdevice@testcsp.net",
                "ipv4Address": {
                    "publicAddress": "233.252.0.2",
                    "privateAddress": "233.252.0.2"
                },
            },
            application_server={"ipv_4_address": "5.6.7.8"},
            qos_profile="QOS_E",
            duration=3600,
        )

        fetched = client.qod.get_session_v_1(session_id=session.session_id)
        assert fetched.session_id == session.session_id

        client.qod.delete_session_v_1(session_id=session.session_id)

    def test_list_sessions_v1(self, client: NetworkAsCodeApi):
        sessions = client.qod.list_sessions_v_1()
        assert sessions is not None
        assert isinstance(sessions, list)

    def test_retrieve_sessions_for_device_v1(self, client: NetworkAsCodeApi):
        session = client.qod.create_session_v_1(
            device={
                "phone_number": "+99999991001",
                "ipv4Address": {
                    "publicAddress": "233.252.0.2",
                    "privateAddress": "233.252.0.2"
                },
            },
            application_server={"ipv_4_address": "8.8.8.8"},
            qos_profile="DOWNLINK_M_UPLINK_L",
            duration=60,
        )

        sessions = client.qod.retrieve_sessions_v_1(
            device={"phone_number": "+99999991001"},
        )
        assert len(sessions) > 0

        client.qod.delete_session_v_1(session_id=session.session_id)

    def test_create_session_with_ports(self, client: NetworkAsCodeApi):
        session = client.qod.create_session_v_1(
            device={
                "network_access_identifier": "testdevice@testcsp.net",
                "ipv4Address": {
                    "publicAddress": "233.252.0.2",
                    "privateAddress": "233.252.0.2"
                },
            },
            application_server={"ipv_4_address": "5.6.7.8"},
            qos_profile="QOS_L",
            duration=3600,
            device_ports={"ports": [80]},
            application_server_ports={"ranges": [{"from_": 80, "to": 443}]},
        )
        assert session is not None
        assert session.qos_profile == "QOS_L"

        client.qod.delete_session(session_id=session.session_id)

    def test_extend_session(self, client: NetworkAsCodeApi):
        session = client.qod.create_session_v_1(
            device={
                "network_access_identifier": "testdevice@testcsp.net",
                "ipv4Address": {
                    "publicAddress": "233.252.0.2",
                    "privateAddress": "233.252.0.2"
                },
            },
            application_server={"ipv_4_address": "5.6.7.8"},
            qos_profile="QOS_L",
            duration=60,
        )

        extended = client.qod.extend_session(
            session_id=session.session_id,
            requested_additional_duration=60,
        )
        assert extended is not None
        assert extended.duration >= 60

        client.qod.delete_session(session_id=session.session_id)

    def test_fail_to_get_deleted_session(self, client: NetworkAsCodeApi):
        session = client.qod.create_session_v_1(
            device={
                "network_access_identifier": "testdevice@testcsp.net",
                "ipv4Address": {
                    "publicAddress": "233.252.0.2",
                    "privateAddress": "233.252.0.2"
                },
            },
            application_server={"ipv_4_address": "5.6.7.8"},
            qos_profile="QOS_E",
            duration=3600,
        )

        client.qod.delete_session(session_id=session.session_id)

        with pytest.raises(Exception):
            client.qod.get_session(session_id=session.session_id)
