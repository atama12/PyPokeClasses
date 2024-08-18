from Models.Utility.Common import *
from typing import List
class Abilities(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/ability/" + str(id))
        
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
    def generation(self):
        return NamedAPIResource(self._json_data["generation"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def effect_entries(self):
        array : List[VerboseEffect] = [VerboseEffect(json_data) for json_data in self._json_data["effect_entries"]]
        return array
    
    @property
    def effect_changes(self):
        array : List[AbilityEffectChange] = [AbilityEffectChange(json_data) for json_data in self._json_data["effect_changes"]]
        return array
    
    @property
    def flavor_text_entries(self):
        array : List[AbilityFlavorText] = [AbilityFlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array
    
    @property
    def pokemon(self):
        array : List[AbilityPokemon] = [AbilityPokemon(json_data) for json_data in self._json_data["pokemon"]]
        return array
    
    
class AbilityEffectChange:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def effect_entries(self):
        array : List[Effect] = [Effect(json_data) for json_data in self.__json_data["effect_entries"]]
        return array

    @property
    def version_group(self):
        return NamedAPIResource(self.__json_data["version_group"])
    
class AbilityFlavorText:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def flavor_text(self):
        return str(self.__json_data["flavor_text"])
    
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])
    
    @property
    def version_group(self):
        return NamedAPIResource(self.__json_data["version_group"])
    
class AbilityPokemon:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def is_hidden(self):
        return bool(self.__json_data["is_hidden"])
    
    @property
    def slot(self):
        return int(self.__json_data["slot"])
    
    @property
    def pokemon(self):
        return NamedAPIResource(self.__json_data["pokemon"])