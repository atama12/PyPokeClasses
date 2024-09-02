from ..Utility.Common import *
from ..Games.Generation import Generation
from ..Moves.MoveLearnMethod import MoveLearnMethod
from .Pokedex import Pokedex
from ..Locations.Region import Region
from .Version import Version

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
        return Generation(self._json_data["generation"]["name"])
    
    @property
    def move_learn_method(self):
        array : List[MoveLearnMethod] = [MoveLearnMethod(json_data["name"]) for json_data in self._json_data["move_learn_method"]]
        return array
    
    @property
    def pokedexes(self):
        array : List[Pokedex] = [Pokedex(json_data["name"]) for json_data in self._json_data["pokedexes"]]
        return array

    @property
    def regions(self):
        array : List[Region] = [Region(json_data["name"]) for json_data in self._json_data["regions"]]
        return array
    
    @property
    def versions(self):
        array : List[Version] = [Version(json_data["name"]) for json_data in self._json_data["versions"]]
        return array
    