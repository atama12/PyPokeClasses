from ..Utility.Common import *
from typing import List

class Language(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/language/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def official(self):
        return bool(self._json_data["official"])
    
    @property
    def iso639(self):
        return str(self._json_data["iso639"])
    
    @property
    def iso3166(self):
        return str(self._json_data["iso3166"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
