import typing_extensions

from devicestatus_client.paths import PathValues
from devicestatus_client.apis.paths.connectivity import Connectivity
from devicestatus_client.apis.paths.event_subscriptions import EventSubscriptions
from devicestatus_client.apis.paths.event_subscriptions_id import EventSubscriptionsId
from devicestatus_client.apis.paths.connectivity_id import ConnectivityId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CONNECTIVITY: Connectivity,
        PathValues.EVENTSUBSCRIPTIONS: EventSubscriptions,
        PathValues.EVENTSUBSCRIPTIONS_ID: EventSubscriptionsId,
        PathValues.CONNECTIVITY_ID: ConnectivityId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CONNECTIVITY: Connectivity,
        PathValues.EVENTSUBSCRIPTIONS: EventSubscriptions,
        PathValues.EVENTSUBSCRIPTIONS_ID: EventSubscriptionsId,
        PathValues.CONNECTIVITY_ID: ConnectivityId,
    }
)
