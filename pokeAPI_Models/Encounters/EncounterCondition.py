from ..Utility.Common import *
from .EncounterConditionValue import EncounterConditionValue
from typing import List

class EncounterCondition(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/encounter-condition/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    

    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def values(self):
        array : List[EncounterConditionValue] = [EncounterConditionValue(json_data["name"]) for json_data in self._json_data["values"]]
        return array


    