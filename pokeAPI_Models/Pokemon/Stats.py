from ..Utility.Common import *
from .Characteristic import Characteristic
from ..Moves.MoveDamageClass import MoveDamageClass
from ..Moves.Moves import Moves
from .Natures import Natures
from typing import List
class Stats(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/stat/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def game_index(self):
        return int(self._json_data["game_index"])
    
    @property
    def is_battle_only(self):
        return bool(self._json_data["is_battle_only"])
    
    @property
    def affecting_moves(self):
        return MoveStatAffectSets(self._json_data["affecting_moves"])
    
    @property
    def affecting_natures(self):
        return NatureStatAffectSets(self._json_data["affecting_natures"])
    
    @property
    def characteristics(self):
        array : List[Characteristic] = [Characteristic(str(json_data["url"]).split('/')[-2]) for json_data in self._json_data["characteristics"]]
        return array
    
    @property
    def move_damage_class(self):
        return MoveDamageClass(self._json_data["move_damage_class"]["name"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array

class MoveStatAffectSets:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def increase(self):
        array : List[MoveStatAffect] = [MoveStatAffect(json_data) for json_data in self.__json_data["increase"]]
        return array
    
    @property
    def decrease(self):
        array : List[MoveStatAffect] = [MoveStatAffect(json_data) for json_data in self.__json_data["decrease"]]
        return array
      
class MoveStatAffect:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def change(self):
        return int(self.__json_data["change"])
    
    @property
    def move(self):
        return Moves(self.__json_data["move"]["name"])  
    
    
class NatureStatAffectSets:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def increase(self):
        array : List[Natures] = [Natures(json_data["name"]) for json_data in self.__json_data["increase"]]
        return array
    
    @property
    def decrease(self):
        array : List[Natures] = [Natures(json_data["name"]) for json_data in self.__json_data["decrease"]]
        return array
