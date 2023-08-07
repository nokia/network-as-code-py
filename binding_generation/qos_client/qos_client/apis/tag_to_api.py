import typing_extensions

from qos_client.apis.tags import TagValues
from qos_client.apis.tags.sessions_api import SessionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SESSIONS: SessionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SESSIONS: SessionsApi,
    }
)
