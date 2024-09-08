import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import Pokemon
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/pokemon.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Pokemon(1)
    test2 = Pokemon(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("id", 1),
    ("name", "bulbasaur"),
    ("abilities[0].ability.name", "overgrow"),
    ("abilities[0].ability.url", "https://pokeapi.co/api/v2/ability/65/"),
    ("abilities[0].is_hidden",False),
    ("abilities[0].slot",1),
    ("base_experience",64),
    ("cries.latest","https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/1.ogg"),
    ("cries.legacy","https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/1.ogg"),
    ("forms[0].name","bulbasaur"),
    ("forms[0].url","https://pokeapi.co/api/v2/pokemon-form/1/"),
    ("game_indices[0].game_index",153),
    ("game_indices[0].version.name","red"),
    ("game_indices[0].version.url","https://pokeapi.co/api/v2/version/1/"),
    ("height",7),
    ("held_items[0].item.name","moon-stone"),
    ("held_items[0].item.url","https://pokeapi.co/api/v2/item/81/"),
    ("held_items[0].version_details[0].rarity",5),
    ("held_items[0].version_details[0].version.name","ruby"),
    ("held_items[0].version_details[0].version.url","https://pokeapi.co/api/v2/version/7/"),
    ("is_default",True),
    ("location_area_encounters", "https://pokeapi.co/api/v2/pokemon/1/encounters"),
    ("moves[0].move.name","razor-wind"),
    ("moves[0].move.url","https://pokeapi.co/api/v2/move/13/"),
    ("moves[0].version_group_details[0].level_learned_at",0),
    ("moves[0].version_group_details[0].move_learn_method.name","egg"),
    ("moves[0].version_group_details[0].move_learn_method.url","https://pokeapi.co/api/v2/move-learn-method/2/"),
    ("moves[0].version_group_details[0].version_group.name","gold-silver"),
    ("moves[0].version_group_details[0].version_group.url","https://pokeapi.co/api/v2/version-group/3/"),
    ("order",1),
    ("past_types[0].generation.name","generation-v"),
    ("past_types[0].generation.url","https://pokeapi.co/api/v2/generation/5/"),
    ("past_types[0].types[0].slot",1),
    ("past_types[0].types[0].type.name","normal"),
    ("past_types[0].types[0].type.url","https://pokeapi.co/api/v2/type/1/"),
    ("species.name","bulbasaur"),
    ("species.url","https://pokeapi.co/api/v2/pokemon-species/1/"),
    ("sprites.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png"),
    ("sprites.back_female",None),
    ("sprites.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/1.png"),
    ("sprites.back_shiny_female",None),
    ("sprites.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"),
    ("sprites.front_female",None),
    ("sprites.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"),
    ("sprites.front_shiny_female",None),
    ("sprites.other.dream_world.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/1.svg"),
    ("sprites.other.dream_world.front_female",None),
    ("sprites.other.home.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png"),
    ("sprites.other.home.front_female",None),
    ("sprites.other.home.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/1.png"),
    ("sprites.other.home.front_shiny_female",None),
    ("sprites.other.official_artwork.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"),
    ("sprites.other.official_artwork.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/1.png"),
    ("sprites.other.showdown.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/back/1.gif"),
    ("sprites.other.showdown.back_female",None),
    ("sprites.other.showdown.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/back/shiny/1.gif"),
    ("sprites.other.showdown.back_shiny_female",None),
    ("sprites.other.showdown.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/1.gif"),
    ("sprites.other.showdown.front_female",None),
    ("sprites.other.showdown.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/shiny/1.gif"),
    ("sprites.other.showdown.front_shiny_female",None),    
    ("sprites.versions.generation_i.red_blue.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/1.png"),
    ("sprites.versions.generation_i.red_blue.back_gray","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/1.png"),
    ("sprites.versions.generation_i.red_blue.back_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/1.png"),
    ("sprites.versions.generation_i.red_blue.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/1.png"),
    ("sprites.versions.generation_i.red_blue.front_gray","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/1.png"),
    ("sprites.versions.generation_i.red_blue.front_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/1.png"),   
    ("sprites.versions.generation_i.yellow.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/1.png"),
    ("sprites.versions.generation_i.yellow.back_gray","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/gray/1.png"),
    ("sprites.versions.generation_i.yellow.back_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/back/1.png"),
    ("sprites.versions.generation_i.yellow.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/1.png"),
    ("sprites.versions.generation_i.yellow.front_gray","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/gray/1.png"),
    ("sprites.versions.generation_i.yellow.front_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/1.png"),   
    ("sprites.versions.generation_ii.crystal.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/1.png"),
    ("sprites.versions.generation_ii.crystal.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/shiny/1.png"),
    ("sprites.versions.generation_ii.crystal.back_shiny_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/shiny/1.png"),
    ("sprites.versions.generation_ii.crystal.back_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/1.png"),
    ("sprites.versions.generation_ii.crystal.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/1.png"),
    ("sprites.versions.generation_ii.crystal.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/shiny/1.png"),
    ("sprites.versions.generation_ii.crystal.front_shiny_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/shiny/1.png"),
    ("sprites.versions.generation_ii.crystal.front_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/1.png"),
    ("sprites.versions.generation_ii.gold.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/1.png"),
    ("sprites.versions.generation_ii.gold.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/shiny/1.png"),
    ("sprites.versions.generation_ii.gold.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/1.png"),
    ("sprites.versions.generation_ii.gold.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/shiny/1.png"),
    ("sprites.versions.generation_ii.gold.front_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/transparent/1.png"),
    ("sprites.versions.generation_ii.silver.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/1.png"),
    ("sprites.versions.generation_ii.silver.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/shiny/1.png"),
    ("sprites.versions.generation_ii.silver.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/1.png"),
    ("sprites.versions.generation_ii.silver.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/shiny/1.png"),
    ("sprites.versions.generation_ii.silver.front_transparent","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/transparent/1.png"),
    ("sprites.versions.generation_iii.emerald.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/1.png"),
    ("sprites.versions.generation_iii.emerald.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/shiny/1.png"),
    ("sprites.versions.generation_iii.firered_leafgreen.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/1.png"),
    ("sprites.versions.generation_iii.firered_leafgreen.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/shiny/1.png"),
    ("sprites.versions.generation_iii.firered_leafgreen.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/1.png"),
    ("sprites.versions.generation_iii.firered_leafgreen.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/shiny/1.png"),
    ("sprites.versions.generation_iii.ruby_sapphire.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/1.png"),
    ("sprites.versions.generation_iii.ruby_sapphire.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/1.png"),
    ("sprites.versions.generation_iii.ruby_sapphire.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/1.png"),
    ("sprites.versions.generation_iii.ruby_sapphire.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/shiny/1.png"),
    ("sprites.versions.generation_iv.diamond_pearl.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/1.png"),
    ("sprites.versions.generation_iv.diamond_pearl.back_female",None),
    ("sprites.versions.generation_iv.diamond_pearl.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/1.png"),
    ("sprites.versions.generation_iv.diamond_pearl.back_shiny_female",None),
    ("sprites.versions.generation_iv.diamond_pearl.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/1.png"),
    ("sprites.versions.generation_iv.diamond_pearl.front_female",None),
    ("sprites.versions.generation_iv.diamond_pearl.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/1.png"),
    ("sprites.versions.generation_iv.diamond_pearl.front_shiny_female",None),
    ("sprites.versions.generation_iv.heartgold_soulsilver.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/1.png"),
    ("sprites.versions.generation_iv.heartgold_soulsilver.back_female",None),
    ("sprites.versions.generation_iv.heartgold_soulsilver.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/1.png"),
    ("sprites.versions.generation_iv.heartgold_soulsilver.back_shiny_female",None),
    ("sprites.versions.generation_iv.heartgold_soulsilver.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/1.png"),
    ("sprites.versions.generation_iv.heartgold_soulsilver.front_female",None),
    ("sprites.versions.generation_iv.heartgold_soulsilver.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/1.png"),
    ("sprites.versions.generation_iv.heartgold_soulsilver.front_shiny_female",None),
    ("sprites.versions.generation_iv.platinum.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/1.png"),
    ("sprites.versions.generation_iv.platinum.back_female",None),
    ("sprites.versions.generation_iv.platinum.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/1.png"),
    ("sprites.versions.generation_iv.platinum.back_shiny_female",None),
    ("sprites.versions.generation_iv.platinum.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/1.png"),
    ("sprites.versions.generation_iv.platinum.front_female",None),
    ("sprites.versions.generation_iv.platinum.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/1.png"),
    ("sprites.versions.generation_iv.platinum.front_shiny_female",None),
    ("sprites.versions.generation_v.black_white.animated.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/1.gif"),
    ("sprites.versions.generation_v.black_white.animated.back_female",None),
    ("sprites.versions.generation_v.black_white.animated.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/1.gif"),
    ("sprites.versions.generation_v.black_white.animated.back_shiny_female",None),
    ("sprites.versions.generation_v.black_white.animated.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/1.gif"),
    ("sprites.versions.generation_v.black_white.animated.front_female",None),
    ("sprites.versions.generation_v.black_white.animated.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/1.gif"),
    ("sprites.versions.generation_v.black_white.animated.front_shiny_female",None),
    ("sprites.versions.generation_v.black_white.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/1.png"),
    ("sprites.versions.generation_v.black_white.back_female",None),
    ("sprites.versions.generation_v.black_white.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/shiny/1.png"),
    ("sprites.versions.generation_v.black_white.back_shiny_female",None),
    ("sprites.versions.generation_v.black_white.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/1.png"),
    ("sprites.versions.generation_v.black_white.front_female",None),
    ("sprites.versions.generation_v.black_white.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/shiny/1.png"),
    ("sprites.versions.generation_v.black_white.front_shiny_female",None),
    ("sprites.versions.generation_vi.omegaruby_alphasapphire.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/1.png"),
    ("sprites.versions.generation_vi.omegaruby_alphasapphire.front_female",None),
    ("sprites.versions.generation_vi.omegaruby_alphasapphire.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/1.png"),
    ("sprites.versions.generation_vi.omegaruby_alphasapphire.front_shiny_female",None),
    ("sprites.versions.generation_vi.x_y.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/1.png"),
    ("sprites.versions.generation_vi.x_y.front_female",None),
    ("sprites.versions.generation_vi.x_y.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/shiny/1.png"),
    ("sprites.versions.generation_vi.x_y.front_shiny_female",None),
    ("sprites.versions.generation_vii.icons.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/1.png"),
    ("sprites.versions.generation_vii.icons.front_female",None),
    ("sprites.versions.generation_vii.ultra_sun_ultra_moon.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/1.png"),
    ("sprites.versions.generation_vii.ultra_sun_ultra_moon.front_female",None),
    ("sprites.versions.generation_vii.ultra_sun_ultra_moon.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/1.png"),
    ("sprites.versions.generation_vii.ultra_sun_ultra_moon.front_shiny_female",None),
    ("sprites.versions.generation_viii.icons.front_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/1.png"),
    ("sprites.versions.generation_viii.icons.front_female",None),
    ("stats[0].base_stat",45),
    ("stats[0].effort",0),
    ("stats[0].stat.name","hp"),
    ("stats[0].stat.url","https://pokeapi.co/api/v2/stat/1/"),
    ("types[0].slot",1),
    ("types[0].type.name","grass"),
    ("types[0].type.url","https://pokeapi.co/api/v2/type/12/"),
    ("weight",69)
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Pokemon(1)
    
    # プロパティが正しく設定されているか確認
    assert eval(f"test_data.{property_name}") == expected_value
    
# # 4. JSONデータの型が正しいことを確認するテスト
# @pytest.mark.parametrize("property_name, expected_type", [
#     ("name", str),
#     ("abilities", list),
#     ("types", list),
#     ("id", int),
# ])
# @patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')
# def test_type_check(mock_make_request, property_name, expected_type, mock_response_data):
#     mock_make_request.return_value = (200, mock_response_data)

#     pikachu = Pokemon(1)
    
#     # 各プロパティの型が正しいことを確認
#     assert isinstance(getattr(pikachu, property_name), expected_type)