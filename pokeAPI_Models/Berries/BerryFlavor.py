from ..Utility.Common import *
from ..Contests.ContestType import ContestType
from .Berry import Berry
from typing import List

class BerryFlavor(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/berry-flavor/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])

    @property
    def berries(self):
        array : List[FlavorBerryMap] = [FlavorBerryMap(json_data) for json_data in self._json_data["berries"]]
        return array
    
    @property
    def contest_type(self):
        return ContestType(self._json_data["contest_type"]["name"])

    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
class FlavorBerryMap:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def potency(self):
        return int(self.__json_data["potency"])
    
    @property
    def berry(self):
        return Berry(self.__json_data["berry"]["name"])
    