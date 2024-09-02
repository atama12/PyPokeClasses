from ..Utility.Common import *
from ..Pokemon.Abilities import AbilityEffectChange
from ..Contests.ContestType import ContestType
from ..Contests.ContestEffect import ContestEffect
from .MoveDamageClass import MoveDamageClass
from ..Pokemon.Pokemon import Pokemon
from ..Games.Generation import Generation
from ..Contests.SuperContestEffect import SuperContestEffect
from .MoveTarget import MoveTarget
from ..Pokemon.Types import Types
from ..Moves.Moves import Moves
from ..Utility.Language import Language
from ..Games.VersionGroup import VersionGroup
from .MoveAilments import MoveAilments
from .MoveCategory import MoveCategory
from ..Pokemon.Stats import Stats
from ..Pokemon.Types import Types
from typing import List
class Moves(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/move/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def accuracy(self):
        return int(self._json_data["accuracy"])
    
    @property
    def effect_chance(self):
        return int(self._json_data["effect_chance"])
    
    @property
    def pp(self):
        return int(self._json_data["pp"])
    
    @property
    def priority(self):
        return int(self._json_data["priority"])    
    
    @property
    def power(self):
        return int(self._json_data["power"])   
    
    @property
    def contest_combos(self):
        return ContestComboSets(self._json_data["contest_combos"])   
    
    @property
    def contest_type(self):
        return ContestType(self._json_data["contest_type"]["name"])

    @property
    def contest_effect(self):
        return ContestEffect(str(self._json_data["contest_effect"]["url"]).split('/')[-2])  
    
    @property
    def damage_class(self):
        return MoveDamageClass(self._json_data["damage_class"]["name"])
      
    @property
    def effect_entries(self):
        array : List[VerboseEffect] = [VerboseEffect(json_data) for json_data in self._json_data["effect_entries"]]
        return array
    
    @property
    def effect_changes(self):
        array : List[AbilityEffectChange] = [AbilityEffectChange(json_data) for json_data in self._json_data["effect_changes"]]
        return array
    
    @property
    def learned_by_pokemon(self):
        array : List[Pokemon] = [Pokemon(json_data["name"]) for json_data in self._json_data["learned_by_pokemon"]]
        return array
    
    @property
    def flavor_text_entries(self):
        array : List[MoveFlavorText] = [MoveFlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array
    
    @property
    def generation(self):
        return Generation(self._json_data["generation"]["name"])

    @property
    def machines(self):
        array : List[MachineVersionDetail] = [MachineVersionDetail(json_data) for json_data in self._json_data["machines"]]
        return array
    
    @property
    def meta(self):
        return MoveMetaData(self._json_data["meta"])  
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def past_values(self):
        array : List[PastMoveStatValues] = [PastMoveStatValues(json_data) for json_data in self._json_data["past_values"]]
        return array
    
    @property
    def stat_changes(self):
        array : List[MoveStatChange] = [MoveStatChange(json_data) for json_data in self._json_data["stat_changes"]]
        return array
    
    @property
    def super_contest_effect(self):
        return SuperContestEffect(str(self._json_data["super_contest_effect"]["url"]).split('/')[-2]) 
    
    @property
    def target(self):
        return MoveTarget(self._json_data["target"]["name"]) 
    
    @property
    def type(self):
        return Types(self._json_data["type"]["name"]) 
    
class ContestComboSets:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def normal(self):
        return ContestComboDetail(self.__json_data["normal"])
    
    @property
    def super(self):
        return ContestComboDetail(self.__json_data["super"])  
    
class ContestComboDetail:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def use_before(self):
        return Moves(self.__json_data["use_before"]["name"])
    
    @property
    def use_after(self):
        return Moves(self.__json_data["use_after"]["name"])  
    
class MoveFlavorText:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def flavor_text(self):
        return str(self.__json_data["flavor_text"])
    
    @property
    def language(self):
        return Language(self.__json_data["language"]["name"])  
    
    @property
    def version_group(self):
        return VersionGroup(self.__json_data["version_group"]["name"])  
    
class MoveMetaData:
    def __init__(self,json_data):
        self.__json_data = json_data
    
    @property
    def ailment(self):
        return MoveAilments(self.__json_data["ailment"]["name"])  
    
    @property
    def category(self):
        return MoveCategory(self.__json_data["category"]["name"])  
    
    @property
    def min_hits(self):
        return int(self.__json_data["min_hits"])  
    
    @property
    def max_hits(self):
        return int(self.__json_data["max_hits"])  
    
    @property
    def min_turns(self):
        return int(self.__json_data["min_turns"])  
    
    @property
    def max_turns(self):
        return int(self.__json_data["max_turns"])  
    
    @property
    def drain(self):
        return int(self.__json_data["drain"])  
    
    @property
    def healing(self):
        return int(self.__json_data["healing"])  
    
    @property
    def crit_rate(self):
        return int(self.__json_data["crit_rate"])  
    
    @property
    def ailment_chance(self):
        return int(self.__json_data["ailment_chance"])  
    
    @property
    def flinch_chance(self):
        return int(self.__json_data["flinch_chance"])  
    
    @property
    def stat_chance(self):
        return int(self.__json_data["stat_chance"])  
    
    
class MoveStatChange:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def change(self):
        return int(self.__json_data["change"])
    
    @property
    def stat(self):
        return Stats(self.__json_data["stat"]["name"])  
    
class PastMoveStatValues:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def accuracy(self):
        return int(self.__json_data["accuracy"])
    
    @property
    def effect_chance(self):
        return int(self.__json_data["effect_chance"])
    
    @property
    def power(self):
        return int(self.__json_data["power"])
    
    @property
    def pp(self):
        return int(self.__json_data["pp"])
    

    @property
    def effect_entries(self):
        array : List[VerboseEffect] = [VerboseEffect(json_data) for json_data in self.__json_data["effect_entries"]]
        return array
    
    @property
    def type(self):
        return Types(self.__json_data["type"]["name"])  
    
    @property
    def version_group(self):
        return VersionGroup(self.__json_data["version_group"]["name"])  
    
