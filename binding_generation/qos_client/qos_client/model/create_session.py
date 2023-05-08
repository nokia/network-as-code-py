# coding: utf-8

"""
    QoS

    QoS manages communication bandwidth for a given device.  # noqa: E501

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


class CreateSession(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "qosProfile",
            "appIp",
            "ip",
            "id",
        }
        
        class properties:
            qosProfile = schemas.StrSchema
            id = schemas.StrSchema
            ip = schemas.StrSchema
            appIp = schemas.StrSchema
        
            @staticmethod
            def devicePorts() -> typing.Type['PortsSpec']:
                return PortsSpec
        
            @staticmethod
            def applicationServerPorts() -> typing.Type['PortsSpec']:
                return PortsSpec
            
            
            class duration(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 86400
                    inclusive_minimum = 1
            notificationUrl = schemas.StrSchema
            __annotations__ = {
                "qosProfile": qosProfile,
                "id": id,
                "ip": ip,
                "appIp": appIp,
                "devicePorts": devicePorts,
                "applicationServerPorts": applicationServerPorts,
                "duration": duration,
                "notificationUrl": notificationUrl,
            }
    
    qosProfile: MetaOapg.properties.qosProfile
    appIp: MetaOapg.properties.appIp
    ip: MetaOapg.properties.ip
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qosProfile"]) -> MetaOapg.properties.qosProfile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appIp"]) -> MetaOapg.properties.appIp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devicePorts"]) -> 'PortsSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationServerPorts"]) -> 'PortsSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationUrl"]) -> MetaOapg.properties.notificationUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["qosProfile", "id", "ip", "appIp", "devicePorts", "applicationServerPorts", "duration", "notificationUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qosProfile"]) -> MetaOapg.properties.qosProfile: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appIp"]) -> MetaOapg.properties.appIp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devicePorts"]) -> typing.Union['PortsSpec', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationServerPorts"]) -> typing.Union['PortsSpec', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationUrl"]) -> typing.Union[MetaOapg.properties.notificationUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["qosProfile", "id", "ip", "appIp", "devicePorts", "applicationServerPorts", "duration", "notificationUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        qosProfile: typing.Union[MetaOapg.properties.qosProfile, str, ],
        appIp: typing.Union[MetaOapg.properties.appIp, str, ],
        ip: typing.Union[MetaOapg.properties.ip, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        devicePorts: typing.Union['PortsSpec', schemas.Unset] = schemas.unset,
        applicationServerPorts: typing.Union['PortsSpec', schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        notificationUrl: typing.Union[MetaOapg.properties.notificationUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateSession':
        return super().__new__(
            cls,
            *args,
            qosProfile=qosProfile,
            appIp=appIp,
            ip=ip,
            id=id,
            devicePorts=devicePorts,
            applicationServerPorts=applicationServerPorts,
            duration=duration,
            notificationUrl=notificationUrl,
            _configuration=_configuration,
            **kwargs,
        )

from qos_client.model.ports_spec import PortsSpec
