from ..Utility.Common import *
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
        array : List[NamedAPIResource] = [ NamedAPIResource(json_data) for json_data in self._json_data["forms"]]
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
        return NamedAPIResource(self._json_data["species"])
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
        return int(self.__json_data["slot"])
    
    @property
    def ability(self):
        return NamedAPIResource(self.__json_data["ability"])
    
class PokemonType:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def slot(self):
        return int(self.__json_data["slot"])
    
    @property
    def type(self):
        return NamedAPIResource(self.__json_data["type"])
    
class PokemonFormType:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def slot(self):
        return int(self.__json_data["slot"])
    
    @property
    def type(self):
        return NamedAPIResource(self.__json_data["type"])
    
class PokemonTypePast:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def generation(self):
        return NamedAPIResource(self.__json_data["generation"])
    
    @property
    def types(self):
        array : List[PokemonType] = [PokemonType(json_data) for json_data in self._json_data["types"]]
        return array

class PokemonHeldItem:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def item(self):
        return NamedAPIResource(self.__json_data["item"])
    
    @property
    def version_details(self):
        array : List[PokemonHeldItemVersion] = [PokemonHeldItemVersion(json_data) for json_data in self._json_data["version_details"]]
        return array
    
class PokemonHeldItemVersion:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def version(self):
        return NamedAPIResource(self.__json_data["version"])
    
    @property
    def rarity(self):
        return int(self.__json_data["rarity"])
    
class PokemonMove:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def move(self):
        return NamedAPIResource(self.__json_data["move"])
    
    @property
    def version_group_details(self):
        array : List[PokemonMoveVersion] = [PokemonMoveVersion(json_data) for json_data in self.__json_data["version_group_details"]]
        return array
    
class PokemonMoveVersion:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def move_learn_method(self):
        return NamedAPIResource(self.__json_data["move_learn_method"])

    @property
    def version_group(self):
        return NamedAPIResource(self.__json_data["version_group"])
        
    @property
    def level_learned_at(self):
        return int(self.__json_data["level_learned_at"])
    
class PokemonStat:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def stat(self):
        return NamedAPIResource(self.__json_data["stat"])
        
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
    
    @property
    def other(self):
        return PokemonSpritesOther(self.__json_data["other"])
    
    @property
    def versions(self):
        return PokemonSpritesVersion(self.__json_data["versions"])

class PokemonSpritesVersion:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def generation_i(self):
        return PokemonSpritesVersionGi(self.__json_data["generation-i"])

    @property
    def generation_ii(self):
        return PokemonSpritesVersionGii(self.__json_data["generation-ii"])

    @property
    def generation_iii(self):
        return PokemonSpritesVersionGiii(self.__json_data["generation-iii"])

    @property
    def generation_iv(self):
        return PokemonSpritesVersionGiv(self.__json_data["generation-iv"])

    @property
    def generation_v(self):
        return PokemonSpritesVersionGv(self.__json_data["generation-v"])

    @property
    def generation_vi(self):
        return PokemonSpritesVersionGvi(self.__json_data["generation-vi"])

    @property
    def generation_vii(self):
        return PokemonSpritesVersionGvii(self.__json_data["generation-vii"])

    @property
    def generation_viii(self):
        return PokemonSpritesVersionGviii(self.__json_data["generation-viii"])

class PokemonSpritesVersionGi:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def red_blue(self):
        return PokemonSpritesRedBlueYellow(self.__json_data["red-blue"])
    
    @property
    def yellow(self):
        return PokemonSpritesRedBlueYellow(self.__json_data["yellow"])

class PokemonSpritesVersionGii:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def crystal(self):
        return PokemonSpritesCrystal(self.__json_data["crystal"])
    
    @property
    def gold(self):
        return PokemonSpritesGoldSilver(self.__json_data["gold"])

    @property
    def silver(self):
        return PokemonSpritesGoldSilver(self.__json_data["silver"])

class PokemonSpritesVersionGiii:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def emerald(self):
        return PokemonSpritesEmerald(self.__json_data["emerald"])
    
    @property
    def firered_leafgreen(self):
        return PokemonSpritesFRRG(self.__json_data["firered-leafgreen"])

    @property
    def ruby_sapphire(self):
        return PokemonSpritesRS(self.__json_data["ruby-sapphire"])

class PokemonSpritesVersionGiv:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def diamond_pearl(self):
        return PokemonSpritesDP(self.__json_data["diamond-pearl"])
    
    @property
    def heartgold_soulsilver(self):
        return PokemonSpritesHGSS(self.__json_data["heartgold-soulsilver"])

    @property
    def platinum(self):
        return PokemonSpritesPt(self.__json_data["platinum"])
       
class PokemonSpritesVersionGv:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def black_white(self):
        return PokemonSpritesBW(self.__json_data["black-white"])
    
class PokemonSpritesVersionGvi:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def omegaruby_alphasapphire(self):
        return PokemonSpritesORAS(self.__json_data["omegaruby-alphasapphire"])
    
    @property
    def x_y(self):
        return PokemonSpritesXY(self.__json_data["x-y"])
    
class PokemonSpritesVersionGvii:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def icons(self):
        return PokemonSpritesIcons(self.__json_data["icons"])
    
    @property
    def ultra_sun_ultra_moon(self):
        return PokemonSpritesUSUM(self.__json_data["ultra-sun-ultra-moon"])
    
class PokemonSpritesVersionGviii:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def icons(self):
        return PokemonSpritesIcons(self.__json_data["icons"])
    
class PokemonSpritesRedBlueYellow:
    def __init__(self,json_data):
        self.__json_data = json_data
    
    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_gray(self):
        return str(self.__json_data["back_gray"])
    
    @property
    def back_transparent(self):
        return str(self.__json_data["back_transparent"])
    
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_gray(self):
        return str(self.__json_data["front_gray"])
    
    @property
    def front_transparent(self):
        return str(self.__json_data["front_transparent"])
    
class PokemonSpritesCrystal:
    def __init__(self,json_data):
        self.__json_data = json_data
    
    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_shiny(self):
        return str(self.__json_data["back_shiny"])
    
    @property
    def back_shiny_transparent(self):
        return str(self.__json_data["back_shiny_transparent"])
    
    @property
    def back_transparent(self):
        return str(self.__json_data["back_transparent"])
    
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def front_shiny_transparent(self):
        return str(self.__json_data["front_shiny_transparent"])
    
    @property
    def front_transparent(self):
        return str(self.__json_data["front_transparent"])

class PokemonSpritesGoldSilver:
    def __init__(self,json_data):
        self.__json_data = json_data
    
    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_shiny(self):
        return str(self.__json_data["back_shiny"])
    
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def front_transparent(self):
        return str(self.__json_data["front_transparent"])
    
class PokemonSpritesEmerald:
    def __init__(self,json_data):
        self.__json_data = json_data
    
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
class PokemonSpritesFRRG:
    def __init__(self,json_data):
        self.__json_data = json_data

    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_shiny(self):
        return str(self.__json_data["back_shiny"])
     
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
class PokemonSpritesRS:
    def __init__(self,json_data):
        self.__json_data = json_data

    @property
    def back_default(self):
        return str(self.__json_data["back_default"])
    
    @property
    def back_shiny(self):
        return str(self.__json_data["back_shiny"])
     
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
class PokemonSpritesDP:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
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
    
class PokemonSpritesHGSS:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
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

class PokemonSpritesPt:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
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

class PokemonSpritesBW:
    def __init__(self,json_data):
        self.__json_data = json_data
       
    @property
    def animated(self):
        return PokemonSpritesAnimated(self.__json_data["animated"])
     
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
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

class PokemonSpritesORAS:
    def __init__(self,json_data):
        self.__json_data = json_data
       
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def front_female(self):
        return str(self.__json_data["front_female"])
    
    @property
    def front_shiny_female(self):
        return str(self.__json_data["front_shiny_female"])
    
class PokemonSpritesXY:
    def __init__(self,json_data):
        self.__json_data = json_data
       
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def front_female(self):
        return str(self.__json_data["front_female"])
    
    @property
    def front_shiny_female(self):
        return str(self.__json_data["front_shiny_female"])

class PokemonSpritesUSUM:
    def __init__(self,json_data):
        self.__json_data = json_data
       
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
    @property
    def front_female(self):
        return str(self.__json_data["front_female"])
    
    @property
    def front_shiny_female(self):
        return str(self.__json_data["front_shiny_female"])

class PokemonSpritesIcons:
    def __init__(self,json_data):
        self.__json_data = json_data
       
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_female(self):
        return str(self.__json_data["front_female"])
    
class PokemonSpritesAnimated:
    def __init__(self,json_data):
        self.__json_data = json_data
       
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
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
    
class PokemonSpritesOther:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def dream_world(self):
        return PokemonSprites2(self.__json_data["dream_world"])
    
    @property
    def home(self):
        return PokemonSprites2(self.__json_data["home"])
    
    @property
    def official_artwork(self):
        return PokemonSprites2(self.__json_data["official-artwork"])
    
    @property
    def showdown(self):
        return PokemonSprites2(self.__json_data["showdown"])
    
class PokemonSprites2:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def front_default(self):
        return str(self.__json_data["front_default"])
    
    @property
    def front_shiny(self):
        return str(self.__json_data["front_shiny"])
    
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