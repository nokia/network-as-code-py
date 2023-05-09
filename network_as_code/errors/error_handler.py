
def error_handler(func, arg, key=None):
    from ..errors import DeviceNotFound, AuthenticationException, ServiceError, InvalidParameter
    from urllib.error import HTTPError
    from pydantic import ValidationError
    from qos_client.exceptions import ApiException


    try:
        if key is not None:
            return func(key=arg)
        else:
            res = func(arg)
            return res
    except ApiException as e:
        if e.status >= 500:
            raise ServiceError(e)
        elif e.status == 422:
            raise InvalidParameter(e)
    except HTTPError as e:
        if e.code == 403:
            raise AuthenticationException(e)
        elif e.code == 404:
            raise DeviceNotFound(e)
        else:
            raise ServiceError(e)
    except ValidationError as e:
        raise InvalidParameter(e)