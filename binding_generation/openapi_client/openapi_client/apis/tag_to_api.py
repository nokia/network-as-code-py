import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.qos_api import QosApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.QOS: QosApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.QOS: QosApi,
    }
)
