from ..Utility.Common import *
from typing import List

class Location(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/location/" + str(id))
        
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def region(self):
        return NamedAPIResource(self._json_data["region"])
  
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array

    @property
    def game_indices(self):
        array : List[GenerationGameIndex] = [GenerationGameIndex(json_data) for json_data in self._json_data["game_indices"]]
        return array
    
    @property
    def areas(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["areas"]]
        return array