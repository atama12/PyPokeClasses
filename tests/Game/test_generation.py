import pytest
from unittest.mock import patch
from pokeAPI_Models.Games import Generation
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Game/files/generation.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Generation(1)
    test2 = Generation(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("abilities[0].name","aaa"),
    ("abilities[0].url","bbb"),
    ("id",1),
    ("main_region.name","kanto"),
    ("main_region.url","https://pokeapi.co/api/v2/region/1/"),
    ("moves[0].name","pound"),
    ("moves[0].url","https://pokeapi.co/api/v2/move/1/"),
    ("name","generation-i"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","\u3060\u3044\u3044\u3061\u305b\u3060\u3044"),
    ("pokemon_species[0].name","bulbasaur"),
    ("pokemon_species[0].url","https://pokeapi.co/api/v2/pokemon-species/1/"),
    ("types[0].name","normal"),
    ("types[0].url","https://pokeapi.co/api/v2/type/1/"),
    ("version_groups[0].name","red-blue"),
    ("version_groups[0].url","https://pokeapi.co/api/v2/version-group/1/"),
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Generation(1)
    
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