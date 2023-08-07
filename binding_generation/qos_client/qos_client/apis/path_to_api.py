import typing_extensions

from qos_client.paths import PathValues
from qos_client.apis.paths.sessions_session_id import SessionsSessionId
from qos_client.apis.paths.sessions import Sessions
from qos_client.apis.paths.sessions_id import SessionsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SESSIONS_SESSION_ID: SessionsSessionId,
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_ID: SessionsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SESSIONS_SESSION_ID: SessionsSessionId,
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_ID: SessionsId,
    }
)
