import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import Stats
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/stat.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Stats(1)
    test2 = Stats(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("affecting_moves.increase[0].change", -1),
    ("affecting_moves.increase[0].move.name", "growl"),
    ("affecting_moves.increase[0].move.url", "https://pokeapi.co/api/v2/move/45/"),
    ("affecting_moves.decrease[0].change", 2),
    ("affecting_moves.decrease[0].move.name", "swords-dance"),
    ("affecting_moves.decrease[0].move.url", "https://pokeapi.co/api/v2/move/14/"),
    ("affecting_natures.increase[0].name", "lonely"),
    ("affecting_natures.increase[0].url", "https://pokeapi.co/api/v2/nature/6/"),
    ("affecting_natures.decrease[0].name", "bold"),
    ("affecting_natures.decrease[0].url", "https://pokeapi.co/api/v2/nature/2/"),
    ("characteristics[0].url", "https://pokeapi.co/api/v2/characteristic/1/"),
    ("game_index", 1),
    ("id", 1),
    ("is_battle_only", False),
    ("move_damage_class", None),
    ("name","hp"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","HP"),
    

])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Stats(1)
    
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