from ..Utility.Common import *
from typing import List

class Item(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/item/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def cost(self):
        return int(self._json_data["cost"])
    
    @property
    def fling_power(self):
        return int(self._json_data["fling_power"])
    
    @property
    def fling_effect(self):
        return NamedAPIResource(self._json_data["fling_effect"])
    
    @property
    def attributes(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["attributes"]]
        return array
    
    @property
    def category(self):
        return NamedAPIResource(self._json_data["category"])
    
    @property
    def effect_entries(self):
        array : List[VerboseEffect] = [VerboseEffect(json_data) for json_data in self._json_data["effect_entries"]]
        return array
    
    @property
    def flavor_text_entries(self):
        array : List[VersionGroupFlavorText] = [VersionGroupFlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array

    @property
    def game_indices(self):
        array : List[GenerationGameIndex] = [GenerationGameIndex(json_data) for json_data in self._json_data["game_indices"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def sprites(self):
        return ItemSprites(self._json_data["sprites"])
    
    @property
    def held_by_pokemon(self):
        array : List[ItemHolderPokemon] = [ItemHolderPokemon(json_data) for json_data in self._json_data["held_by_pokemon"]]
        return array
    
    @property
    def baby_trigger_for(self):
        return APIResource(self._json_data["baby_trigger_for"])
    
    @property
    def machines(self):
        array : List[MachineVersionDetail] = [MachineVersionDetail(json_data) for json_data in self._json_data["machines"]]
        return array
     
class ItemSprites:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def default(self):
        return str(self.__json_data["default"])
    
class ItemHolderPokemon:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def pokemon(self):
        return NamedAPIResource(self.__json_data["pokemon"])
    
    @property
    def version_details(self):
        array : List[ItemHolderPokemonVersionDetail] = [ItemHolderPokemonVersionDetail(json_data) for json_data in self.__json_data["version_details"]]
        return array
    
class ItemHolderPokemonVersionDetail:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def rarity(self):
        return int(self.__json_data["rarity"])
    
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])
    