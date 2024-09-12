import pytest
from unittest.mock import patch
from PyPokeClasses.Items import Item
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Item/files/item.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Item(1)
    test2 = Item(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("attributes[0].name","countable"),
    ("attributes[0].url","https://pokeapi.co/api/v2/item-attribute/1/"),
    ("baby_trigger_for.url","aaa"),
    ("category.name","standard-balls"),
    ("category.url","https://pokeapi.co/api/v2/item-category/34/"),
    ("cost",0),
    ("effect_entries[0].effect","Used in battle\n:   Catches a wild Pok\u00e9mon without fail.\n\n    If used in a trainer battle, nothing happens and the ball is lost."),
    ("effect_entries[0].language.name","en"),
    ("effect_entries[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("effect_entries[0].short_effect","Catches a wild Pok\u00e9mon every time."),
    ("flavor_text_entries[0].language.name","en"),
    ("flavor_text_entries[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("flavor_text_entries[0].text","The best BALL that\ncatches a POK\u00e9MON\nwithout fail."),
    ("flavor_text_entries[0].version_group.name","ruby-sapphire"),
    ("flavor_text_entries[0].version_group.url","https://pokeapi.co/api/v2/version-group/5/"),
    ("fling_effect.name","aaa1"),
    ("fling_power",1),
    ("game_indices[0].game_index",1),
    ("game_indices[0].generation.name","generation-iii"),
    ("game_indices[0].generation.url","https://pokeapi.co/api/v2/generation/3/"),
    ("held_by_pokemon[0].pokemon.name","poke_aaa"),
    ("held_by_pokemon[0].pokemon.url","poke_bbb"),
    ("held_by_pokemon[0].version_details[0].rarity",1),
    ("held_by_pokemon[0].version_details[0].version.name","vd_aaa"),
    ("held_by_pokemon[0].version_details[0].version.url","vd_bbb"),
    ("id",1),
    ("machines[0].machine.url","ma_aaa"),
    ("machines[0].version_group.name","vg_aaa"),
    ("machines[0].version_group.url","vg_bbb"),
    ("name","master-ball"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","\u30de\u30b9\u30bf\u30fc\u30dc\u30fc\u30eb"),
    ("sprites.default","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png")
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Item(1)
    
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