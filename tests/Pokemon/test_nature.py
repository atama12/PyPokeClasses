import pytest
from unittest.mock import patch
from PyPokeClasses.Pokemon import Natures
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/nature.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Natures(1)
    test2 = Natures(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("decreased_stat",None),
    ("hates_flavor",None),
    ("id",1),
    ("increased_stat",None),
    ("likes_flavor",None),
    ("move_battle_style_preferences[0].high_hp_preference",61),
    ("move_battle_style_preferences[0].low_hp_preference",61),
    ("move_battle_style_preferences[0].move_battle_style.name","attack"),
    ("move_battle_style_preferences[0].move_battle_style.url","https://pokeapi.co/api/v2/move-battle-style/1/"),
    ("name","hardy"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","\u304c\u3093\u3070\u308a\u3084"),
    ("pokeathlon_stat_changes[0].max_change",-1),
    ("pokeathlon_stat_changes[0].pokeathlon_stat.name","speed"),
    ("pokeathlon_stat_changes[0].pokeathlon_stat.url","https://pokeapi.co/api/v2/pokeathlon-stat/1/"),
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Natures(1)
    
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