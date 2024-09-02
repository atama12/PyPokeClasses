from ..Utility.Common import *
from typing import List

class ContestEffect(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/contest-effect/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def appeal(self):
        return int(self._json_data["appeal"])
    
    @property
    def jam(self):
        return int(self._json_data["jam"])
    
    @property
    def effect_entries(self):
        array : List[Effect] = [Effect(json_data) for json_data in self._json_data["effect_entries"]]
        return array
    
    @property
    def flavor_text_entries(self):
        array : List[FlavorText] = [FlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array
