import typing_extensions

from slice_client.apis.tags import TagValues
from slice_client.apis.tags.default_api import DefaultApi
from slice_client.apis.tags.slice_api import SliceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEFAULT: DefaultApi,
        TagValues.SLICE: SliceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEFAULT: DefaultApi,
        TagValues.SLICE: SliceApi,
    }
)
