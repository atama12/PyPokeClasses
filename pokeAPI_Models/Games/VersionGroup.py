from ..Utility.Common import *
from typing import List

class VersionGroup(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/version-group/" + str(id))
        
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
    def generation(self):
        return NamedAPIResource(self._json_data["generation"])
    
    @property
    def move_learn_method(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["move_learn_method"]]
        return array
    
    @property
    def pokedexes(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["pokedexes"]]
        return array

    @property
    def regions(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["regions"]]
        return array
    
    @property
    def versions(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["versions"]]
        return array
    