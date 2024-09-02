from ..Utility.Common import *
from ..Games.Generation import Generation
from ..Moves.MoveDamageClass import MoveDamageClass
from ..Moves.Moves import Moves
from ..Pokemon.Pokemon import Pokemon
from typing import List
class Types(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/type/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def damage_relations(self):
        return TypeRelations(self._json_data["damage_relations"])
    
    @property
    def past_damage_relations(self):
        array : List[TypeRelationsPast] = [TypeRelationsPast(json_data) for json_data in self._json_data["past_damage_relations"]]
        return array

    @property
    def game_indices(self):
        array : List[GenerationGameIndex] = [GenerationGameIndex(json_data) for json_data in self._json_data["game_indices"]]
        return array
    
    @property
    def generation(self):
        return Generation(self._json_data["generation"]["name"])
    
    @property
    def move_damage_class(self):
        return MoveDamageClass(self._json_data["move_damage_class"]["name"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array

    @property
    def pokemon(self):
        array : List[TypePokemon] = [TypePokemon(json_data) for json_data in self._json_data["pokemon"]]
        return array
    
    @property
    def moves(self):
        array : List[Moves] = [Moves(json_data["name"]) for json_data in self._json_data["moves"]]
        return array
    
class TypePokemon:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def slot(self):
        return int(self.__json_data["slot"])
    
    @property
    def pokemon(self):
        return Pokemon(self.__json_data["pokemon"]["name"])
      
    
    
class TypeRelations:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def no_damage_to(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self.__json_data["no_damage_to"]]
        return array
    
    @property
    def half_damage_to(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self.__json_data["half_damage_to"]]
        return array
    
    @property
    def double_damage_to(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self.__json_data["double_damage_to"]]
        return array
    
    @property
    def no_damage_from(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self.__json_data["no_damage_from"]]
        return array
    
    @property
    def half_damage_from(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self.__json_data["half_damage_from"]]
        return array
    
    @property
    def double_damage_from(self):
        array : List[Types] = [Types(json_data["name"]) for json_data in self.__json_data["double_damage_from"]]
        return array
    
class TypeRelationsPast:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def generation(self):
        return Generation(self.__json_data["generation"]["name"])
    
    @property
    def damage_relations(self):
        return TypeRelations(self.__json_data["damage_relations"])
    
