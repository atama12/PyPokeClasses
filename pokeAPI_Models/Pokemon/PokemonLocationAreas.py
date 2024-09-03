from ..Utility.Common import *
from typing import List
class PokemonLocationAreas(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon/" + str(id) + "/encounters")
        
    @property
    def location_area(self):
        return NamedAPIResource(self._json_data["location_area"])
    
    @property
    def version_details(self):
        array : List[VersionEncounterDetail] = [VersionEncounterDetail(json_data) for json_data in self._json_data["version_details"]]
        return array