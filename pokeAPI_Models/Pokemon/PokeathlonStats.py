from ..Utility.Common import *
from typing import List
class PokeathlonStats(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokeathlon-stat/" + str(id))
        
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
    def affecting_natures(self):
        return NaturePokeathlonStatAffectSets(self._json_data["affecting_natures"])

class NaturePokeathlonStatAffectSets:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def increase(self):
        array : List[NaturePokeathlonStatAffect] = [NaturePokeathlonStatAffect(json_data) for json_data in self.__json_data["increase"]]
        return array
    
    @property
    def decrease(self):
        array : List[NaturePokeathlonStatAffect] = [NaturePokeathlonStatAffect(json_data) for json_data in self.__json_data["decrease"]]
        return array
      
class NaturePokeathlonStatAffect:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def max_change(self):
        return int(self.__json_data["max_change"])
    
    @property
    def nature(self):
        return NamedAPIResource(self.__json_data["nature"])  
    