from ..Utility.Common import *
from .Item import Item
from typing import List

class ItemFlingEffect(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/item-fling-effect/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def effect_entries(self):
        array : List[Effect] = [Effect(json_data) for json_data in self._json_data["effect_entries"]]
        return array
    
    @property
    def items(self):
        array : List[Item] = [Item(json_data["name"]) for json_data in self._json_data["items"]]
        return array
    