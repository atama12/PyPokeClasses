from ..Utility.Common import *
from typing import List

class EncounterMethod(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/encounter-method/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def order(self):
        return int(self._json_data["order"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array


    