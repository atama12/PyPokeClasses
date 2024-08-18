from Models.Utility.Common import *
from .Pokemon import PokemonFormType
from typing import List
class PokemonForms(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon-form/" + str(id))
        
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
    def form_order(self):
        return int(self._json_data["form_order"])
    
    @property
    def is_default(self):
        return bool(self._json_data["is_default"])
    
    @property
    def is_battle_only(self):
        return bool(self._json_data["is_battle_only"])
    
    @property
    def is_mega(self):
        return bool(self._json_data["is_mega"])

    @property
    def form_name(self):
        return str(self._json_data["form_name"])
    
    @property
    def pokemon(self):
        return NamedAPIResource(self._json_data["pokemon"])
    
    @property
    def types(self):
        array : List[PokemonFormType] = [PokemonFormType(json_data) for json_data in self._json_data["types"]]
        return array
    
    @property
    def sprites(self):
        return PokemonFormSprites(self._json_data["sprites"])
    
    @property
    def vertion_group(self):
        return NamedAPIResource(self._json_data["vertion_group"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def form_names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["form_names"]]
        return array
    
    
class PokemonFormSprites:
    def __init__(self,json_data):
        self.__json_data = json_data
        

    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_shiny(self):
        return str(self.__json_data["back_shiny"])
    