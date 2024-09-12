import pytest
from unittest.mock import patch
from pokeAPI_Models.Berries import BerryFlavor
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Berry/files/berry-flavor.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = BerryFlavor(1)
    test2 = BerryFlavor(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("berries[0].berry.name","rowap"),
    ("berries[0].berry.url","https://pokeapi.co/api/v2/berry/64/"),
    ("berries[0].potency",10),
    ("contest_type.name","cool"),
    ("contest_type.url","https://pokeapi.co/api/v2/contest-type/1/"),
    ("id",1),
    ("name","spicy"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","\u304b\u3089\u3044"),
    
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = BerryFlavor(1)
    
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