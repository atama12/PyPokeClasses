from ..Utility.Common import *
from typing import List

class Machine(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/machine/" + str(id))
        
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def item(self):
        return NamedAPIResource(self._json_data["item"])
  
    @property
    def move(self):
        return NamedAPIResource(self._json_data["move"])
    
    @property
    def version_group(self):
        return NamedAPIResource(self._json_data["version_group"])