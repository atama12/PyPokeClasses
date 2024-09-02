from ..Utility.Common import *
from ..Items.Item import Item
from ..Moves.Moves import Moves
from ..Games.VersionGroup import VersionGroup
from typing import List

class Machine(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/machine/" + str(id))
        
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def item(self):
        return Item(self._json_data["item"]["name"])
  
    @property
    def move(self):
        return Moves(self._json_data["move"]["name"])
    
    @property
    def version_group(self):
        return VersionGroup(self._json_data["version_group"]["name"])