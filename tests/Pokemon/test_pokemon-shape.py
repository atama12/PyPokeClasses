import pytest
from unittest.mock import patch
from PyPokeClasses.Pokemon import PokemonShapes
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/pokemon-shape.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = PokemonShapes(1)
    test2 = PokemonShapes(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("id", 1),
    ("name","ball"),
    ("names[0].language.name","fr"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/5/"),
    ("names[0].name","Balle"),
    ("pokemon_species[0].name","shellder"),
    ("pokemon_species[0].url","https://pokeapi.co/api/v2/pokemon-species/90/"),
    ("awesome_names[1].awesome_name","Pomaceous"),
    ("awesome_names[1].language.name","en"),
    ("awesome_names[1].language.url","https://pokeapi.co/api/v2/language/9/"),

    

])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = PokemonShapes(1)
    
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