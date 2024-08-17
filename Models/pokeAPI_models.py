import requests_cache

# requests_cache を有効化
session = requests_cache.CachedSession('pokemon')

class BaseModel:
    def __init__(self,url):
        self._data = session.get(url)
        self._json_data = self._data.json()
        
class NamedAPIResource:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def name(self):
        return str(self.__json_data["name"])
    
    @property
    def url(self):
        return str(self.__json_data["url"])
    
class VersionGameIndex:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def game_index(self):
        return int(self.__json_data["game_index"])
    
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])