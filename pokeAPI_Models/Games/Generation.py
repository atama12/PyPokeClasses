from ..Utility.Common import *
from ..Pokemon.Abilities import Abilities
from ..Locations.Region import Region
from ..Moves.Moves import Moves
from ..Pokemon.PokemonSpecies import PokemonSpecies
from ..Pokemon.Types import Types
from ..Games.VersionGroup import VersionGroup

from typing import List

class Generation(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/generation/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def abilities(self):
        array : List[Abilities] = [Abilities(json_data["name"]) for json_data in self._json_data["abilities"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def main_region(self):
        return Region(self._json_data["main_region"])
    
    @property
    def moves(self):
        array : List[Moves] = [Moves(json_data["name"]) for json_data in self._json_data["moves"]]
        return array

    @property
    def pokemon_species(self):
        array : List[PokemonSpecies] = [PokemonSpecies(json_data["name"]) for json_data in self._json_data["pokemon_species"]]
        return array
    
    @property
    def types(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self._json_data["types"]]
        return array
    
    @property
    def version_groups(self):
        array : List[VersionGroup] = [VersionGroup(json_data["name"]) for json_data in self._json_data["version_groups"]]
        return array