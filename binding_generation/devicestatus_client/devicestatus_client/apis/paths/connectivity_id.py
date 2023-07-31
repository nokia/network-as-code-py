from devicestatus_client.paths.connectivity_id.get import ApiForget
from devicestatus_client.paths.connectivity_id.put import ApiForput
from devicestatus_client.paths.connectivity_id.delete import ApiFordelete


class ConnectivityId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
