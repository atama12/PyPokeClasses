import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import Characteristic
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/characteristic.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Characteristic(1)
    test2 = Characteristic(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("descriptions[0].description", "\u305f\u3079\u308b\u306e\u304c\u3000\u3060\u3044\u3059\u304d"),
    ("descriptions[0].language.name", "ja-Hrkt"),
    ("descriptions[0].language.url", "https://pokeapi.co/api/v2/language/1/"),
    ("gene_modulo",0),
    ("highest_stat.name","hp"),
    ("highest_stat.url","https://pokeapi.co/api/v2/stat/1/"),
    ("id",1),
    ("possible_values[0]",0)
    
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Characteristic(1)
    
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