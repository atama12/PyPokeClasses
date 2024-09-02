from ..Utility.Common import *
from ..Pokemon.PokemonSpecies import PokemonSpecies
from typing import List

class PalParkArea(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pal-park-area/" + str(id))
        
        
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
    def pokemon_encounters(self):
        array : List[PalParkEncounterSpecies] = [PalParkEncounterSpecies(json_data) for json_data in self._json_data["pokemon_encounters"]]
        return array
    

class PalParkEncounterSpecies:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def base_score(self):
        return int(self.__json_data["base_score"])

    @property
    def rate(self):
        return int(self.__json_data["rate"])
    
    @property
    def pokemon_species(self):
        return PokemonSpecies(self.__json_data["pokemon_species"]["name"])
    