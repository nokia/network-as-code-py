import typing_extensions

from qos_client.paths import PathValues
from qos_client.apis.paths.sessions import Sessions
from qos_client.apis.paths.sessions_session_id import SessionsSessionId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_SESSION_ID: SessionsSessionId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_SESSION_ID: SessionsSessionId,
    }
)
