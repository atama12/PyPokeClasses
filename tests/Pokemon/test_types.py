import pytest
from unittest.mock import patch
from PyPokeClasses.Pokemon import Types
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/type.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Types(1)
    test2 = Types(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("damage_relations.double_damage_from[0].name", "fighting"),
    ("damage_relations.double_damage_from[0].url", "https://pokeapi.co/api/v2/type/2/"),
    ("damage_relations.double_damage_to[0].name", "normal"),
    ("damage_relations.double_damage_to[0].url", "https://pokeapi.co/api/v2/type/233/"),
    ("damage_relations.half_damage_from[0].name", "fling"),
    ("damage_relations.half_damage_from[0].url", "https://pokeapi.co/api/v2/type/223/"),
    ("damage_relations.half_damage_to[0].name", "rock"),
    ("damage_relations.half_damage_to[0].url", "https://pokeapi.co/api/v2/type/6/"),
    ("damage_relations.no_damage_from[0].name", "ghost"),
    ("damage_relations.no_damage_from[0].url", "https://pokeapi.co/api/v2/type/8/"),
    ("damage_relations.no_damage_to[0].name", "ghosttt"),
    ("damage_relations.no_damage_to[0].url", "https://pokeapi.co/api/v2/type/8a/"),
    ("game_indices[0].game_index", 0),
    ("game_indices[0].generation.name", "generation-i"),
    ("game_indices[0].generation.url", "https://pokeapi.co/api/v2/generation/1/"),
    ("generation.name", "generation-i"),
    ("generation.url", "https://pokeapi.co/api/v2/generation/1/"),
    ("id",1),
    ("move_damage_class.name","physical"),
    ("move_damage_class.url","https://pokeapi.co/api/v2/move-damage-class/2/"),
    ("moves[0].name","pound"),
    ("moves[0].url","https://pokeapi.co/api/v2/move/1/"),
    ("name","normal"),
    ("names[0].language.name","en"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("names[0].name","Normal"),
    ("past_damage_relations[0].generation.name","generation-v"),
    ("past_damage_relations[0].generation.url","https://pokeapi.co/api/v2/generation/5/"),
    ("past_damage_relations[0].damage_relations.no_damage_to[0].name","normal"),
    ("past_damage_relations[0].damage_relations.no_damage_to[0].url","https://pokeapi.co/api/v2/type/1/"),
    ("past_damage_relations[0].damage_relations.half_damage_to[0].name","steel"),
    ("past_damage_relations[0].damage_relations.half_damage_to[0].url","https://pokeapi.co/api/v2/type/9/"),
    ("past_damage_relations[0].damage_relations.double_damage_to[0].name","ghost"),
    ("past_damage_relations[0].damage_relations.double_damage_to[0].url","https://pokeapi.co/api/v2/type/8/"),
    ("past_damage_relations[0].damage_relations.no_damage_from[0].name","normal"),
    ("past_damage_relations[0].damage_relations.no_damage_from[0].url","https://pokeapi.co/api/v2/type/1/"),
    ("past_damage_relations[0].damage_relations.half_damage_from[0].name","poison"),
    ("past_damage_relations[0].damage_relations.half_damage_from[0].url","https://pokeapi.co/api/v2/type/4/"),
    ("past_damage_relations[0].damage_relations.double_damage_from[0].name","ghost"),
    ("past_damage_relations[0].damage_relations.double_damage_from[0].url","https://pokeapi.co/api/v2/type/8/"),
    ("pokemon[0].pokemon.name","pidgey"),
    ("pokemon[0].pokemon.url","https://pokeapi.co/api/v2/pokemon/16/"),
    ("pokemon[0].slot",1),
    ("sprites.generation_iii.colosseum.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/colosseum/1.png"),
    ("sprites.generation_iii.emerald.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/emerald/1.png"),
    ("sprites.generation_iii.firered_leafgreen.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/firered-leafgreen/1.png"),
    ("sprites.generation_iii.ruby_saphire.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/ruby-saphire/1.png"),
    ("sprites.generation_iii.xd.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iii/xd/1.png"),
    ("sprites.generation_iv.diamond_pearl.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iv/diamond-pearl/1.png"),
    ("sprites.generation_iv.heartgold_soulsilver.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iv/heartgold-soulsilver/1.png"),
    ("sprites.generation_iv.platinum.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-iv/platinum/1.png"),
    ("sprites.generation_v.black_2_white_2.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-v/black-2-white-2/1.png"),
    ("sprites.generation_v.black_white.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-v/black-white/1.png"),
    ("sprites.generation_vi.omega_ruby_alpha_sapphire.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/omega-ruby-alpha-sapphire/1.png"),
    ("sprites.generation_vi.x_y.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vi/x-y/1.png"),
    ("sprites.generation_vii.lets_go_pikachu_lets_go_eevee.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vii/lets-go-pikachu-lets-go-eevee/1.png"),
    ("sprites.generation_vii.sun_moon.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vii/sun-moon/1.png"),
    ("sprites.generation_vii.ultra_sun_ultra_moon.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-vii/ultra-sun-ultra-moon/1.png"),
    ("sprites.generation_viii.brilliant_diamond_and_shining_pearl.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-viii/brilliant-diamond-and-shining-pearl/1.png"),
    ("sprites.generation_viii.legends_arceus.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-viii/legends-arceus/1.png"),
    ("sprites.generation_viii.sword_shield.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-viii/sword-shield/1.png"),
    ("sprites.generation_ix.scarlet_violet.name_icon","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/types/generation-ix/scarlet-violet/1.png"),
    
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Types(1)
    
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