# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slice_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SLICES = "/slices"
    SLICES_ID = "/slices/{id}"
    SLICES_ID_ACTIVATE = "/slices/{id}/activate"
    SLICES_ID_DEACTIVATE = "/slices/{id}/deactivate"
