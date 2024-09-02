from ..Utility.Common import *
from ..Moves.Moves import Moves
from typing import List

class SuperContestEffect(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/super-contest-effect/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def appeal(self):
        return int(self._json_data["appeal"])
    
    @property
    def flavor_text_entries(self):
        array : List[FlavorText] = [FlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array
    
    @property
    def moves(self):
        array : List[Moves] = [Moves(json_data["name"]) for json_data in self._json_data["moves"]]
        return array
