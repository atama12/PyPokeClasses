import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import PokemonForms
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/pokemon-form.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = PokemonForms(1)
    test2 = PokemonForms(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("form_name",""),
    ("form_names",[]),
    ("form_order",1),
    ("id",1),
    ("is_battle_only",False),
    ("is_default",True),
    ("is_mega",False),
    ("name","bulbasaur"),
    ("names",[]),
    ("order",1),
    ("pokemon.name","bulbasaur"),
    ("pokemon.url","https://pokeapi.co/api/v2/pokemon/1/"),
    ("sprites.back_default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png"),
    ("sprites.back_female",None),
    ("sprites.back_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/1.png"),
    ("sprites.back_shiny_female",None),
    ("sprites.front_default", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"),
    ("sprites.front_female",None),
    ("sprites.front_shiny","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png"),
    ("sprites.front_shiny_female",None),
    ("types[0].slot",1),
    ("types[0].type.name","grass"),
    ("types[0].type.url","https://pokeapi.co/api/v2/type/12/"),
    ("version_group.name","red-blue"),
    ("version_group.url","https://pokeapi.co/api/v2/version-group/1/"),
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = PokemonForms(1)
    
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