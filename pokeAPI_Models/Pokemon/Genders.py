from ..Utility.Common import *
from typing import List
class Genders(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/gender/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def pokemon_species_details(self):
        array : List[PokemonSpeciesGender] = [PokemonSpeciesGender(json_data) for json_data in self._json_data["pokemon_species_details"]]
        return array
    
    @property
    def required_for_evolution(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["required_for_evolution"]]
        return array
    
    
class PokemonSpeciesGender:
    def __init__(self,json_data):
        self.__json_data = json_data
        

    @property
    def rate(self):
        return int(self.__json_data["rate"])
    
    @property
    def pokemon_species(self):
        return NamedAPIResource(self.__json_data["pokemon_species"])