import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import PokemonLocationAreas
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/pokemon-encounters.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = PokemonLocationAreas(1)
    test2 = PokemonLocationAreas(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
# @pytest.mark.parametrize("property_name, expected_value", [
#     ("[0].location_area.name", "cerulean-city-area"),
#     ("[0].location_area.url", "https://pokeapi.co/api/v2/location-area/281/"),
#     ("[0].version_details[0].encounters_details[0].chance", 100),
#     ("[0].version_details[0].encounters_details[0].condition_values[0].name", "time-morning"),
#     ("[0].version_details[0].encounters_details[0].condition_values[0].url", "https://pokeapi.co/api/v2/encounter-condition-value/3/"),
#     ("[0].version_details[0].encounters_details[0].max_level", 10),
#     ("[0].version_details[0].encounters_details[0].min_level", 10),
#     ("[0].version_details[0].encounters_details[0].method.name", "gift"),
#     ("[0].version_details[0].encounters_details[0].method.url", "https://pokeapi.co/api/v2/encounter-method/18/"),
#     ("[0].version_details[0].max_chance", 100),
#     ("[0].version_details[0].version.name", "yellow"),
#     ("[0].version_details[0].version.url", "https://pokeapi.co/api/v2/version/3/"),

    

# ])
# @patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

# def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
#     mock_make_request.return_value = (mock_response_data)

#     test_data = PokemonLocationAreas(1)
    
#     # プロパティが正しく設定されているか確認
#     assert eval(f"test_data{property_name}") == expected_value
    
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