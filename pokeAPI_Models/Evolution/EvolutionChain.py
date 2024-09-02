from ..Utility.Common import *
from ..Items.Item import Item
from ..Pokemon.PokemonSpecies import PokemonSpecies
from .EvolutionTrigger import EvolutionTrigger
from ..Moves.Moves import Moves
from ..Pokemon.Types import Types
from ..Locations.Location import Location


from typing import List

class EvolutionChain(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/evolution-chain/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def baby_trigger_item(self):
        return Item(self._json_data["baby_trigger_item"]["name"])
    
    @property
    def chain(self):
        return ChainLink(self._json_data["chain"])
    
    
class ChainLink:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def is_baby(self):
        return bool(self.__json_data["is_baby"])
    
    @property
    def species(self):
        return PokemonSpecies(self.__json_data["species"]["name"])
    
    @property
    def evolution_details(self):
        array : List[EvolutionDetail] = [EvolutionDetail(json_data) for json_data in self.__json_data["evolution_details"]]
        return array
    
    @property
    def evolves_to(self):
        array : List[ChainLink] = [ChainLink(json_data) for json_data in self.__json_data["evolves_to"]]
        return array
    
class EvolutionDetail:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def item(self):
        return Item(self.__json_data["item"]["name"])
    
    @property
    def trigger(self):
        return EvolutionTrigger(self.__json_data["trigger"]["name"])
    
    @property
    def gender(self):
        return int(self.__json_data["gender"])
    
    @property
    def held_item(self):
        return Item(self.__json_data["held_item"]["name"])
    
    @property
    def known_move(self):
        return Moves(self.__json_data["known_move"]["name"])
    
    @property
    def known_move_type(self):
        return Types(self.__json_data["known_move_type"]["name"])
    
    @property
    def location(self):
        return Location(self.__json_data["location"]["name"])
    
    @property
    def min_level(self):
        return int(self.__json_data["min_level"])
  
    @property
    def min_happiness(self):
        return int(self.__json_data["min_happiness"])
 
    @property
    def min_beauty(self):
        return int(self.__json_data["min_beauty"])
 
    @property
    def min_affection(self):
        return int(self.__json_data["min_affection"])
   
    @property
    def needs_overworld_rain(self):
        return int(self.__json_data["needs_overworld_rain"])
    
    @property
    def party_species(self):
        return PokemonSpecies(self.__json_data["party_species"]["name"])
    
    @property
    def party_type(self):
        return Types(self.__json_data["party_type"]["name"])
    
    @property
    def relative_physical_stats(self):
        return int(self.__json_data["relative_physical_stats"])
   
    @property
    def time_of_day(self):
        return str(self.__json_data["time_of_day"])
   
    @property
    def trade_species(self):
        return PokemonSpecies(self.__json_data["trade_species"]["name"])
   
    @property
    def turn_upside_down(self):
        return bool(self.__json_data["turn_upside_down"])
   