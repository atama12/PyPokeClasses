from ..Utility.Common import *
from ..Berries.BerryFlavor import BerryFlavor
from ..Utility.Language import Language
from typing import List

class ContestType(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/contest-type/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def berry_flavor(self):
        return BerryFlavor(self._json_data["berry_flavor"]["name"])
    
    @property
    def names(self):
        array : List[ContestName] = [ContestName(json_data) for json_data in self._json_data["names"]]
        return array

class ContestName:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def name(self):
        return str(self.__json_data["name"])
    
    @property
    def color(self):
        return str(self.__json_data["color"])
    
    @property
    def language(self):
        return Language(self.__json_data["language"]["name"])
    