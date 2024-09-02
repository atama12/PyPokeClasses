from ..Utility.Common import *
from .PokemonForms import PokemonForms
from .PokemonSpecies import PokemonSpecies
from .Abilities import Abilities
from .Types import Types
from ..Games.Generation import Generation
from ..Items.Item import Item
from ..Games.Version import Version
from ..Moves.Moves import Moves
from ..Moves.MoveLearnMethod import MoveLearnMethod
from ..Games.VersionGroup import VersionGroup
from .Stats import Stats
from typing import List

class Pokemon(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    @property
    def base_experience(self):
        return int(self._json_data["base_experience"])
    @property
    def height(self):
        return int(self._json_data["height"])
    @property
    def is_default(self):
        return bool(self._json_data["is_default"])
    @property
    def order(self):
        return int(self._json_data["order"])
    @property
    def weight(self):
        return int(self._json_data["weight"])
    @property
    def abilities(self):
        array : List[PokemonAbility] = [ PokemonAbility(json_data) for json_data in self._json_data["abilities"]]
        return array
    
    @property
    def forms(self):
        array : List[PokemonForms] = [ PokemonForms(json_data["name"]) for json_data in self._json_data["forms"]]
        return array
    
    @property
    def game_indices(self):
        array : List[VersionGameIndex] = [ VersionGameIndex(json_data) for json_data in self._json_data["game_indices"]]
        return array
    @property
    def held_items(self):
        array : List[PokemonHeldItem] = [PokemonHeldItem(json_data) for json_data in self._json_data["held_items"]]
        return array
    @property
    def location_area_encounters(self):
        return str(self._json_data["location_area_encounters"])
    @property
    def moves(self):
        array : List[PokemonMove] = [PokemonMove(json_data) for json_data in self._json_data["moves"]]
        return array
    @property
    def past_types(self):
        array : List[PokemonTypePast] = [PokemonTypePast(json_data) for json_data in self._json_data["past_types"]]
        return array
    @property
    def sprites(self):
        return PokemonSprites(self._json_data["sprites"])
    @property
    def cries(self):
        return PokemonCries(self._json_data["cries"])
    @property
    def species(self):
        return PokemonSpecies(self._json_data["species"]["name"])
    @property
    def stats(self):
        array : List[PokemonStat] = [PokemonStat(json_data) for json_data in self._json_data["stats"]]
        return array
    @property
    def types(self):
        array : List[PokemonType] = [PokemonType(json_data) for json_data in self._json_data["types"]]
        return array
    
class PokemonAbility:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def is_hidden(self):
        return bool(self.__json_data["is_hidden"])
    
    @property
    def slot(self):
        return int(self.__json_data["is_hidden"])
    
    @property
    def ability(self):
        return Abilities(self.__json_data["ability"]["name"])
    
class PokemonType:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def slot(self):
        return int(self.__json_data["slot"])
    
    @property
    def type(self):
        return Types(self.__json_data["type"]["name"])
    
class PokemonFormType:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def slot(self):
        return int(self.__json_data["slot"])
    
    @property
    def type(self):
        return Types(self.__json_data["type"]["name"])
    
class PokemonTypePast:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def generation(self):
        return Generation(self.__json_data["generation"]["name"])
    
    @property
    def types(self):
        array : List[PokemonType] = [PokemonType(json_data) for json_data in self._json_data["types"]]
        return array

class PokemonHeldItem:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def item(self):
        return Item(self.__json_data["item"]["name"])
    
    @property
    def version_details(self):
        array : List[PokemonHeldItemVersion] = [PokemonHeldItemVersion(json_data) for json_data in self._json_data["version_details"]]
        return array
    
class PokemonHeldItemVersion:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def version(self):
        return Version(self.__json_data["version"]["name"])
    
    @property
    def rarity(self):
        return int(self.__json_data["rarity"])
    
class PokemonMove:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def move(self):
        return Moves(self.__json_data["move"]["name"])
    
    @property
    def version_group_details(self):
        array : List[PokemonMoveVersion] = [PokemonMoveVersion(json_data) for json_data in self._json_data["version_group_details"]]
        return array
    
class PokemonMoveVersion:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def move_learn_method(self):
        return MoveLearnMethod(self.__json_data["move_learn_method"]["name"])

    @property
    def version_group(self):
        return VersionGroup(self.__json_data["version_group"]["name"])
        
    @property
    def level_learned_at(self):
        return int(self.__json_data["level_learned_at"])
    
class PokemonStat:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def stat(self):
        return Stats(self.__json_data["stat"]["name"])
        
    @property
    def effort(self):
        return int(self.__json_data["effort"])
    
    @property
    def base_stat(self):
        return int(self.__json_data["base_stat"])
    
class PokemonSprites:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_female(self):
        return str(self.__json_data["front_female"])
    
    @property
    def front_shiny_female(self):
        return str(self.__json_data["front_shiny_female"])
    
    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_shiny(self):
        return str(self.__json_data["back_shiny"])
    
    @property
    def back_female(self):
        return str(self.__json_data["back_female"])
    
    @property
    def back_shiny_female(self):
        return str(self.__json_data["back_shiny_female"])
    

class PokemonCries:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def latest(self):
        return str(self.__json_data["latest"])
        
    @property
    def legacy(self):
        return str(self.__json_data["legacy"])