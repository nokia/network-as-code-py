# coding: utf-8

"""
    QoS on Demand

    Manage QoS sessions for users on demand.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from qos_client import schemas  # noqa: F401


class EventDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "qosStatus",
            "statusInfo",
            "sessionId",
        }
        
        class properties:
            sessionId = schemas.StrSchema
        
            @staticmethod
            def qosStatus() -> typing.Type['EventQosStatus']:
                return EventQosStatus
        
            @staticmethod
            def statusInfo() -> typing.Type['StatusInfo']:
                return StatusInfo
            __annotations__ = {
                "sessionId": sessionId,
                "qosStatus": qosStatus,
                "statusInfo": statusInfo,
            }
    
    qosStatus: 'EventQosStatus'
    statusInfo: 'StatusInfo'
    sessionId: MetaOapg.properties.sessionId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qosStatus"]) -> 'EventQosStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusInfo"]) -> 'StatusInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sessionId", "qosStatus", "statusInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qosStatus"]) -> 'EventQosStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusInfo"]) -> 'StatusInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sessionId", "qosStatus", "statusInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        qosStatus: 'EventQosStatus',
        statusInfo: 'StatusInfo',
        sessionId: typing.Union[MetaOapg.properties.sessionId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventDetail':
        return super().__new__(
            cls,
            *args,
            qosStatus=qosStatus,
            statusInfo=statusInfo,
            sessionId=sessionId,
            _configuration=_configuration,
            **kwargs,
        )

from qos_client.model.event_qos_status import EventQosStatus
from qos_client.model.status_info import StatusInfo
