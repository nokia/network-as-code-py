import typing_extensions

from location_client.paths import PathValues
from location_client.apis.paths.verify import Verify
from location_client.apis.paths.get import Get

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.VERIFY: Verify,
        PathValues.GET: Get,
    }
)

path_to_api = PathToApi(
    {
        PathValues.VERIFY: Verify,
        PathValues.GET: Get,
    }
)
