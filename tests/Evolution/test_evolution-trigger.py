import pytest
from unittest.mock import patch
from PyPokeClasses.Evolution import EvolutionTrigger
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Evolution/files/evolution-trigger.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = EvolutionTrigger(1)
    test2 = EvolutionTrigger(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("id",1),
    ("name","level-up"),
    ("names[0].language.name","fr"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/5/"),
    ("names[0].name","Mont\u00e9e de niveau"),
    ("pokemon_species[0].name","ivysaur"),
    ("pokemon_species[0].url","https://pokeapi.co/api/v2/pokemon-species/2/"),
    
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = EvolutionTrigger(1)
    
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