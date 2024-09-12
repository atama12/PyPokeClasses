import pytest
from unittest.mock import patch
from pokeAPI_Models.Berries import Berry
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Berry/files/berry.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Berry(1)
    test2 = Berry(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("firmness.name","soft"),
    ("firmness.url","https://pokeapi.co/api/v2/berry-firmness/2/"),
    ("flavors[0].flavor.name","spicy"),
    ("flavors[0].flavor.url","https://pokeapi.co/api/v2/berry-flavor/1/"),
    ("flavors[0].potency",10),
    ("growth_time",3),
    ("id",1),
    ("item.name","cheri-berry"),
    ("item.url","https://pokeapi.co/api/v2/item/126/"),
    ("max_harvest",5),
    ("name","cheri"),
    ("natural_gift_power",60),
    ("natural_gift_type.name","fire"),
    ("natural_gift_type.url","https://pokeapi.co/api/v2/type/10/"),
    ("size",20),
    ("smoothness",25),
    ("soil_dryness",15),
    
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Berry(1)
    
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