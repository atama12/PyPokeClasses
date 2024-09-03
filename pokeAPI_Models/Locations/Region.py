from ..Utility.Common import *
from typing import List

class Region(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/region/" + str(id))
        
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def locations(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["locations"]]
        return array
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array

    @property
    def main_generation(self):
        return NamedAPIResource(self._json_data["main_generation"])

    @property
    def pokedexes(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["pokedexes"]]
        return array
    
    @property
    def version_groups(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["version_groups"]]
        return array
    