
from . import Namespace
from ..models import Session
from ..errors import error_handler

class Sessions(Namespace):
    """Representation of a mobile subscription.

    Through this class many of the parameters of a
    subscription can be configured on the network.
    """

    def get(self, id: str) -> Session:
        """Get a QoS Session by its ID.

        Args:
            id (str): ID of the QoS Session 
        """
        # Error Case: Getting session
        response = error_handler(func=self.api.sessions.get_session, arg={ 'sessionId': id})
        # session_object = response.body
        session_object = self.api.sessions.get_session({ 'sessionId': id})

        return Session.convert_session_model(self.api, "",  session_object.json())
