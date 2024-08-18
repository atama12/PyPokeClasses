from .pokeAPI_models import BaseModel,NamedAPIResource,VersionGameIndex
from typing import List
class PokemonSpecies(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/pokemon-species/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def order(self):
        return int(self._json_data["order"])
    
    @property
    def gender_rate(self):
        return int(self._json_data["gender_rate"])
    @property
    def capture_rate(self):
        return int(self._json_data["capture_rate"])
    @property
    def base_happiness(self):
        return int(self._json_data["base_happiness"])
    @property
    def is_baby(self):
        return bool(self._json_data["is_baby"])
    @property
    def is_legendary(self):
        return bool(self._json_data["is_legendary"])
    
    @property
    def is_mythical(self):
        return bool(self._json_data["is_mythical"])
    
    @property
    def hatch_counter(self):
        return int(self._json_data["hatch_counter"])

    @property
    def has_gender_differences(self):
        return bool(self._json_data["has_gender_differences"])
    @property
    def forms_switchable(self):
        return bool(self._json_data["forms_switchable"])
    @property
    def growth_rate(self):
        return NamedAPIResource(self._json_data["growth_rate"])
    # @property
    # def pokedex_numbers(self):
    #     array : List[PokemonAbility] = [ PokemonAbility(json_data) for json_data in self._json_data["abilities"]]
    #     return array
    @property
    def egg_groups(self):
        array : List[NamedAPIResource] = [ NamedAPIResource(json_data) for json_data in self._json_data["egg_groups"]]
        return array
    
    @property
    def color(self):
        return NamedAPIResource(self._json_data["color"])
    
    @property
    def shape(self):
        return NamedAPIResource(self._json_data["shape"])
    
    @property
    def evolves_from_species(self):
        return NamedAPIResource(self._json_data["evolves_from_species"])
    