# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slice_client.paths.slices_id import Api

from slice_client.paths import PathValues

path = PathValues.SLICES_ID