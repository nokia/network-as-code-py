import os
import httpx

from typing import Optional

class SliceAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.rapid_key = rapid_key
        self.rapid_host = rapid_host
        self.client = httpx.Client(base_url=base_url)   


    def create(self,body):
        response = self.client.post(
            url="/slices",
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            },
            data=body
        )

        response.raise_for_status()

        return response
    

    def getAll(self):
        res = self.client.get(
            url="/slices",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )

        res.raise_for_status()

        return res
    
    def get(self, slice_id: str):
        res = self.client.get(
            url=f"/slices/{slice_id}",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )

        res.raise_for_status()

        return res

    def activate(self, slice_id: str):
        res = self.client.post(
            url=f"/slices/{slice_id}/activate",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )

        res.raise_for_status()

        return res
    
    def deactivate(self, slice_id: str):
        return self.client.post(
            url=f"/slices/{slice_id}/deactivate",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )
    
    def delete(self, slice_id: str):
        res = self.client.post(
            url=f"/slices/{slice_id}/delete",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )

        res.raise_for_status()

        return res
    
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

class AttachAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.rapid_key = rapid_key
        self.rapid_host = rapid_host
        self.client = httpx.Client(base_url=base_url, headers={"X-RapidAPI-Key": rapid_key, "X-RapidAPI-Host": rapid_host})   

    def attach(self, device, slice_id: str, notification_url: str, notification_auth_token: Optional[str] = None):
        res = self.client.post(
            url=f"/slice/{slice_id}/attach",
            json=delete_none({
                "phoneNumber": device.phone_number,
                "notificationUrl": notification_url,
                "notificationAuthToken": notification_auth_token
            })
        )

        res.raise_for_status()
    
    def detach(self, device, slice_id: str, notification_url: str, notification_auth_token: Optional[str] = None):
        res = self.client.post(
            url=f"/slice/{slice_id}/detach",
            json=delete_none({
                "phoneNumber": device.phone_number,
                "notificationUrl": notification_url,
                "notificationAuthToken": notification_auth_token
            })
        )

        res.raise_for_status()

