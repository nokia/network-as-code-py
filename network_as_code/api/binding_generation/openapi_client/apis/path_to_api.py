import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.sessions import Sessions

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SESSIONS: Sessions,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SESSIONS: Sessions,
    }
)
