from ..Utility.Common import *
from .GrowthRate import GrowthRate
from .EggGroup import EggGroup
from .PokemonColors import PokemonColors
from .PokemonShapes import PokemonShapes
from .PokemonSpecies import PokemonSpecies
from ..Evolution.EvolutionChain import EvolutionChain
from .PokemonHabitats import PokemonHabitats
from ..Games.Generation import Generation
from ..Utility.Language import Language
from ..Games.Pokedex import Pokedex
from ..Locations.PalParkArea import PalParkArea
from ..Pokemon.Pokemon import Pokemon
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
        return GrowthRate(self._json_data["growth_rate"]["name"])
    @property
    def pokedex_numbers(self):
        array : List[PokemonSpeciesDexEntry] = [ PokemonSpeciesDexEntry(json_data) for json_data in self._json_data["pokedex_numbers"]]
        return array
    @property
    def egg_groups(self):
        array : List[EggGroup] = [ EggGroup(json_data["name"]) for json_data in self._json_data["egg_groups"]]
        return array
    
    @property
    def color(self):
        return PokemonColors(self._json_data["color"]["name"])
    
    @property
    def shape(self):
        return PokemonShapes(self._json_data["shape"]["name"])
    
    @property
    def evolves_from_species(self):
        return PokemonSpecies(self._json_data["evolves_from_species"]["name"])
    
    @property
    def evolution_chain(self):
        return EvolutionChain(str(self._json_data["evolution_chain"]["url"]).split('/')[-2])
    
    @property
    def habitat(self):
        return PokemonHabitats(self._json_data["habitat"]["name"])
    
    @property
    def generation(self):
        return Generation(self._json_data["generation"]["name"])
    
    @property
    def names(self):
        array : List[Name] = [Name(json_data) for json_data in self._json_data["names"]]
        return array
    
    @property
    def pal_park_encounters(self):
        array : List[PalParkEncounterArea] = [PalParkEncounterArea(json_data) for json_data in self._json_data["pal_park_encounters"]]
        return array
    @property
    def flavor_text_entries(self):
        array : List[FlavorText] = [FlavorText(json_data) for json_data in self._json_data["flavor_text_entries"]]
        return array    
    @property
    def form_descriptions(self):
        array : List[Description] = [Description(json_data) for json_data in self._json_data["form_descriptions"]]
        return array
    @property
    def genera(self):
        array : List[Genus] = [Genus(json_data) for json_data in self._json_data["genera"]]
        return array
    @property
    def varieties(self):
        array : List[PokemonSpeciesVariety] = [PokemonSpeciesVariety(json_data) for json_data in self._json_data["varieties"]]
        return array
    
    
class Genus:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def genus(self):
        return str(self.__json_data["genus"])
    
    @property
    def language(self):
        return Language(self.__json_data["language"]["name"])    
    
class PokemonSpeciesDexEntry:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def entry_number(self):
        return int(self.__json_data["entry_number"])
    
    @property
    def pokedex(self):
        return Pokedex(self.__json_data["pokedex"]["name"])
    
class PalParkEncounterArea:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def base_score(self):
        return int(self.__json_data["base_score"])
    @property
    def rate(self):
        return int(self.__json_data["rate"])
    @property
    def area(self):
        return PalParkArea(self.__json_data["area"]["name"])
    
class PokemonSpeciesVariety:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def is_default(self):
        return bool(self.__json_data["is_default"])

    @property
    def pokemon(self):
        return Pokemon(self.__json_data["pokemon"]["name"])