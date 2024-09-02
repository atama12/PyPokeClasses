from ..Utility.Common import *
from .BerryFirmness import BerryFirmness
from .BerryFlavor import BerryFlavor
from ..Items.Item import Item
from ..Pokemon.Types import Types
from typing import List

class Berry(BaseModel):
    def __init__(self,id):
        super().__init__("https://pokeapi.co/api/v2/berry/" + str(id))
        
    @property
    def id(self):
        return int(self._json_data["id"])
    
    @property
    def name(self):
        return str(self._json_data["name"])
    
    @property
    def growth_time(self):
        return int(self._json_data["growth_time"])
    
    @property
    def max_harvest(self):
        return int(self._json_data["max_harvest"])
    
    @property
    def natural_gift_power(self):
        return int(self._json_data["natural_gift_power"])
    
    @property
    def size(self):
        return int(self._json_data["size"])
    
    @property
    def smoothness(self):
        return int(self._json_data["smoothness"])
    
    @property
    def soil_dryness(self):
        return int(self._json_data["soil_dryness"])
    
    @property
    def firmness(self):
        return BerryFirmness(self._json_data["firmness"]["name"])
    
    @property
    def flavors(self):
        array : List[BerryFlavorMap] = [BerryFlavorMap(json_data) for json_data in self._json_data["flavors"]]
        return array
    
    @property
    def item(self):
        return Item(self._json_data["item"]["name"])
    
    @property
    def natural_gift_type(self):
        return Types(self._json_data["natural_gift_type"]["name"])
    
class BerryFlavorMap:
    def __init__(self,json_data):
        self.__json_data = json_data
        
    @property
    def potency(self):
        return int(self.__json_data["potency"])
    
    @property
    def flavor(self):
        return BerryFlavor(self.__json_data["flavor"]["name"])
    