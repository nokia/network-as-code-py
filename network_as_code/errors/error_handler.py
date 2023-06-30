from qos_client.model.session_info import SessionInfo


def error_handler(func, arg, key=None) -> SessionInfo:
    """An error handler function. 
    
    Returns success response or raises error when the given function has exception.
    
    ### Args:
        func(Any): A function which will be called by the error handler
        arg(Any): Argument list of the provided function
        key(Any): Key for the argument (default None)

    ### Example:
    ```python
        response = error_handler(func=self.api.sessions.get_session, arg={ 'sessionId': id})
    ```
    """

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