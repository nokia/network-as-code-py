import os
import httpx


class SliceAPI:
    def __init__(self, base_url: str, rapid_key: str, rapid_host: str) -> None:
        self.rapid_key = rapid_key
        self.rapid_host = rapid_host
        self.client = httpx.Client(base_url=base_url, verify=False)   


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
        return response
    

    def getAll(self):
        return self.client.get(
            url="/slices",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )
    
    def get(self, slice_id: str):
        return self.client.get(
            url=f"/slices/{slice_id}",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )

    def activate(self, slice_id: str):
        return self.client.post(
            url=f"/slices/{slice_id}/activate",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )
    
    def deactivate(self, slice_id: str):
        return self.client.post(
            url=f"/slices/{slice_id}/deactivate",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )
    
    def delete(self, slice_id: str):
        return self.client.post(
            url=f"/slices/{slice_id}/delete",
            headers={
                'X-RapidAPI-Key': self.rapid_key,
                'X-RapidAPI-Host': self.rapid_host
            }
        )