from ..Utility.Common import *
from .Stats import Stats
from ..Berries.BerryFlavor import BerryFlavor
from ..Moves.MoveBattleStyles import MoveBattleStyles
from typing import List
class Natures(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/nature/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def decreased_stat(self):
        return Stats(self._json_data["decreased_stat"]["name"])
    
    @property
    def increased_stat(self):
        return Stats(self._json_data["increased_stat"]["name"])

    @property
    def hates_flavor(self):
        return BerryFlavor(self._json_data["hates_flavor"]["name"])

    @property
    def likes_flavor(self):
        return BerryFlavor(self._json_data["likes_flavor"]["name"])
    
    @property
    def pokeathlon_stat_changes(self):
        array : List[NatureStatChange] = [NatureStatChange(json_data) for json_data in self._json_data["pokeathlon_stat_changes"]]
        return array
    
    @property
    def move_battle_style_preferences(self):
        array : List[MoveBattleStylePreference] = [MoveBattleStylePreference(json_data) for json_data in self._json_data["move_battle_style_preferences"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
class NatureStatChange:
    def __init__(self,json_data):
        self.__json_data = json_data
        

    @property
    def max_change(self):
        return int(self.__json_data["max_change"])
    
    @property
    def pokeathlon_stat(self):
        return NamedAPIResource(self.__json_data["pokeathlon_stat"])
    
class MoveBattleStylePreference:
    def __init__(self,json_data):
        self.__json_data = json_data
        

    @property
    def low_hp_preference(self):
        return int(self.__json_data["low_hp_preference"])
    
    @property
    def high_hp_preference(self):
        return int(self.__json_data["high_hp_preference"])
    
    @property
    def move_battle_style(self):
        return MoveBattleStyles(self.__json_data["move_battle_style"]["name"])