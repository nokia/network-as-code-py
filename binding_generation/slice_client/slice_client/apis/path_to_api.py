import typing_extensions

from slice_client.paths import PathValues
from slice_client.apis.paths.slices import Slices
from slice_client.apis.paths.slices_id import SlicesId
from slice_client.apis.paths.slices_id_activate import SlicesIdActivate
from slice_client.apis.paths.slices_id_deactivate import SlicesIdDeactivate

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SLICES: Slices,
        PathValues.SLICES_ID: SlicesId,
        PathValues.SLICES_ID_ACTIVATE: SlicesIdActivate,
        PathValues.SLICES_ID_DEACTIVATE: SlicesIdDeactivate,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SLICES: Slices,
        PathValues.SLICES_ID: SlicesId,
        PathValues.SLICES_ID_ACTIVATE: SlicesIdActivate,
        PathValues.SLICES_ID_DEACTIVATE: SlicesIdDeactivate,
    }
)
