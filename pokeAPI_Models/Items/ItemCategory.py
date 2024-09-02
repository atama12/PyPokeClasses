from ..Utility.Common import *
from .Item import Item
from .ItemPocket import ItemPocket
from typing import List

class ItemCategory(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/item-category/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def items(self):
        array : List[Item] = [Item(json_data["name"]) for json_data in self._json_data["items"]]
        return array
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def pocket(self):
        return ItemPocket(self._json_data["pocket"]["name"])
    
