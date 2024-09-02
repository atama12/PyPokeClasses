from ..Utility.Common import *
from ..Locations.Region import Region
from .VersionGroup import VersionGroup
from ..Pokemon.PokemonSpecies import PokemonSpecies
from typing import List

class Pokedex(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokedex/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def is_main_series(self):
        return bool(self._json_data["is_main_series"])
    
    @property
    def descriptions(self):
        array : List[Description] = [Description(json_data) for json_data in self._json_data["descriptions"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def pokemon_entries(self):
        array : List[PokemonEntry] = [PokemonEntry(json_data) for json_data in self._json_data["pokemon_entries"]]
        return array
    
    @property
    def region(self):
        return Region(self._json_data["region"]["name"])
    
    @property
    def version_groups(self):
        array : List[VersionGroup] = [VersionGroup(json_data["name"]) for json_data in self._json_data["version_groups"]]
        return array
    
    
    
class PokemonEntry:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def entry_number(self):
        return int(self.__json_data["entry_number"])
    
    @property
    def pokemon_species(self):
        return PokemonSpecies(self.__json_data["pokemon_species"]["name"])
    