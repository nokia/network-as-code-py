import typing_extensions

from location_client.apis.tags import TagValues
from location_client.apis.tags.location_api import LocationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LOCATION: LocationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LOCATION: LocationApi,
    }
)
