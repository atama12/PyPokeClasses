from Models.Utility.Common import *
from typing import List
class Characteristic(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/characteristic/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def gene_modulo(self):
        return int(self._json_data["gene_modulo"])

    @property
    def possible_values(self):  
        array : List[int] = [int(json_data) for json_data in self._json_data["possible_values"]]
        return array
    
    @property
    def highest_stat(self):
        return NamedAPIResource(self._json_data["highest_stat"])
    
    @property
    def descriptions(self):  
        array : List[Description] = [Description(json_data) for json_data in self._json_data["descriptions"]]
        return array