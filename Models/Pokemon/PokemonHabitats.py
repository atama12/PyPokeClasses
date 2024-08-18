from Models.Utility.Common import *
from typing import List
class PokemonHabitats(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon-habitat/" + str(id))
        
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
    def pokemon_species(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["pokemon_species"]]
        return array
    
    
