from Models.Utility.Common import *
from typing import List
class GrowthRate(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/growth-rate/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def formula(self):
        return str(self._json_data["formula"])
    
    @property
    def descriptions(self):
        array : List[Description] = [Description(json_data) for json_data in self._json_data["descriptions"]]
        return array
    
    @property
    def levels(self):
        array : List[GrowthRateExperienceLevel] = [GrowthRateExperienceLevel(json_data) for json_data in self._json_data["levels"]]
        return array
    
    @property
    def pokemon_species(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self._json_data["pokemon_species"]]
        return array
    
    
class GrowthRateExperienceLevel:
    def __init__(self,json_data):
        self.__json_data = json_data
        

    @property
    def level(self):
        return int(self.__json_data["level"])
    
    @property
    def experience(self):
        return int(self.__json_data["experience"])
    