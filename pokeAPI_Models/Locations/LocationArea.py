from ..Utility.Common import *
from typing import List

class LocationArea(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/location-area/" + str(id))
        
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def game_index(self):
        return int(self._json_data["game_index"])
    
    @property
    def encounter_method_rates(self):
        array : List[EncounterMethodRate] = [EncounterMethodRate(json_data) for json_data in self._json_data["encounter_method_rates"]]
        return array

    @property
    def location(self):
        return NamedAPIResource(self._json_data["location"])
    
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def pokemon_encounters(self):
        array : List[PokemonEncounter] = [PokemonEncounter(json_data) for json_data in self._json_data["pokemon_encounters"]]
        return array

class EncounterMethodRate:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def encounter_method(self):
        return NamedAPIResource(self.__json_data["encounter_method"])
    
    @property
    def version_details(self):
        array : List[EncounterVersionDetails] = [EncounterVersionDetails(json_data) for json_data in self.__json_data["version_details"]]
        return array
    
class EncounterVersionDetails:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def rate(self):
        return int(self.__json_data["rate"])
    
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])
    
class PokemonEncounter:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def pokemon(self):
        return NamedAPIResource(self.__json_data["pokemon"])
    
    @property
    def version_details(self):
        array : List[VersionEncounterDetail] = [VersionEncounterDetail(json_data) for json_data in self.__json_data["version_details"]]
        return array
    
