from ..Utility.Common import *
from typing import List
class PokemonShapes(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon-shape/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def awesome_names(self):
        array : List[AwesomeName] = [AwesomeName(json_data) for json_data in self._json_data["awesome_names"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def pokemon_species(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["pokemon_species"]]
        return array
    
class AwesomeName:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def awesome_name(self):
        return str(self.__json_data["awesome_name"])
    
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])  
    
