
import httpx

def delete_none(_dict):
    """Delete None values recursively from all of the dictionaries"""
    for key, value in list(_dict.items()):
        if isinstance(value, dict):
            delete_none(value)
        elif value is None:
            del _dict[key]
        elif isinstance(value, list):
            for v_i in value:
                if isinstance(v_i, dict):
                    delete_none(v_i)

    return _dict


def httpx_client(base_url: str, rapid_key: str, rapid_host: str):
    return httpx.Client(
        base_url=base_url,
        headers={
                "content-type": "application/json",
                "X-RapidAPI-Key": rapid_key,
                "X-RapidAPI-Host": rapid_host,
        },
    )
