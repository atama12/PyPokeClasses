import requests_cache
from typing import List
# requests_cache を有効化
session = requests_cache.CachedSession('pokemon')

class BaseModel:
    def __init__(self,url):
        self.__data = session.get(url)
        self._json_data = self.__data.json()
        


class APIResource:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def url(self):
        return str(self.__json_data["url"])
    
class Description:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def description(self):
        return str(self.__json_data["description"])
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])

class Effect:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def effect(self):
        return str(self.__json_data["effect"])
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])
    
class Encounter:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def min_level(self):
        return int(self.__json_data["min_level"])
    
    @property
    def max_level(self):
        return int(self.__json_data["max_level"])
    
    @property
    def condition_values(self):
        array : List[NamedAPIResource] = [NamedAPIResource(json_data) for json_data in self.__json_data["condition_values"]]
        return array
    
    @property
    def chance(self):
        return int(self.__json_data["chance"])
    
    @property
    def method(self):
        return NamedAPIResource(self.__json_data["method"])
    
class FlavorText:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def flavor_text(self):
        return str(self.__json_data["flavor_text"])
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])
   
   
class GenerationGameIndex:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def game_index(self):
        return int(self.__json_data["game_index"])
    @property
    def generation(self):
        return NamedAPIResource(self.__json_data["generation"])

 
class Name:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def name(self):
        return str(self.__json_data["name"])
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])

class NamedAPIResource:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def name(self):
        return str(self.__json_data["name"])
    
    @property
    def url(self):
        return str(self.__json_data["url"])
    
class VerboseEffect:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def effect(self):
        return str(self.__json_data["effect"])
    
    @property
    def short_effect(self):
        return str(self.__json_data["short_effect"])
    
    @property
    def language(self):
        return NamedAPIResource(self.__json_data["language"])
    
class VersionGameIndex:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def game_index(self):
        return int(self.__json_data["game_index"])
    
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])
    
class VersionEncounterDetail:
    def __init__(self,json_data):
        self.__json_data = json_data

    
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])
    
    @property
    def max_chance(self):
        return int(self.__json_data["max_chance"])
    
    @property
    def encounter_details(self):
        array : List[Encounter] = [Encounter(json_data) for json_data in self.__json_data["encounter_details"]]
        return array