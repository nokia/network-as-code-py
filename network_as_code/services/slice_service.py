
from typing import Dict, List
from network_as_code.models.slice import AreaOfService, NetworkIdentifier, Point, SliceInfo, Throughput


class SliceService:
    @staticmethod
    def network_identifier(networkIdentifierDict: Dict[str, str]):
        return NetworkIdentifier(mcc=networkIdentifierDict['mcc'], mnc=networkIdentifierDict['mnc'])
    
    @staticmethod
    def slice_info(sliceInfoDict: Dict[str, str]):
        return SliceInfo(service_type=sliceInfoDict['service_type'], differentiator=sliceInfoDict['differentiator'])
    
    @staticmethod
    def area_of_service(areaOfServiceDict: Dict[str, List[Dict[str, int]]]):
        poligon = areaOfServiceDict['poligon']
        return AreaOfService(poligon=[Point(latitude=poligon[0]['lat'], longitude=poligon[0]['lon']), Point(latitude=poligon[1]['lat'], longitude=poligon[1]['lon']), Point(latitude=poligon[2]['lat'], longitude=poligon[2]['lon']), Point(latitude=poligon[3]['lat'], longitude=poligon[3]['lon'])])

    @staticmethod
    def throughput(throughputdict: Dict[int, int]):
        return Throughput(guaranteed=throughputdict['guaranteed'], maximum=throughputdict['maximum'])