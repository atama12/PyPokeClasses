import pytest
from unittest.mock import patch
from PyPokeClasses.Locations import LocationArea
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Location/files/location-area.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = LocationArea(1)
    test2 = LocationArea(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("encounter_method_rates[0].encounter_method.name","old-rod"),
    ("encounter_method_rates[0].encounter_method.url","https://pokeapi.co/api/v2/encounter-method/2/"),
    ("encounter_method_rates[0].version_details[0].rate",25),
    ("encounter_method_rates[0].version_details[0].version.name","diamond"),
    ("encounter_method_rates[0].version_details[0].version.url","https://pokeapi.co/api/v2/version/12/"),
    ("game_index",1),
    ("id",1),
    ("location.name","canalave-city"),
    ("location.url","https://pokeapi.co/api/v2/location/1/"),
    ("name","canalave-city-area"),
    ("names[0].language.name","en"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("names[0].name","Canalave City"),
    ("pokemon_encounters[0].pokemon.name","tentacool"),
    ("pokemon_encounters[0].pokemon.url","https://pokeapi.co/api/v2/pokemon/72/"),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].chance",60),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].condition_values[0].name","aaa"),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].condition_values[0].url","bbb"),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].max_level",30),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].min_level",20),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].method.name","surf"),
    ("pokemon_encounters[0].version_details[0].encounter_details[0].method.url","https://pokeapi.co/api/v2/encounter-method/5/"),
    ("pokemon_encounters[0].version_details[0].max_chance",60),
    ("pokemon_encounters[0].version_details[0].version.name","diamond"),
    ("pokemon_encounters[0].version_details[0].version.url","https://pokeapi.co/api/v2/version/12/"),
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = LocationArea(1)
    
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