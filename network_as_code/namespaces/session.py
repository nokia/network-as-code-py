from . import Namespace
from ..models import QoDSession
from ..errors import error_handler


class Sessions(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    def get(self, id: str) -> QoDSession:
        """Get a QoS Session by its ID.

        Args:
            id (str): ID of the QoS Session
        """
        session_object = self.api.sessions.get_session(id)

        return QoDSession.convert_session_model(self.api, "", session_object.json())
