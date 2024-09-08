import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import Abilities
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/ability.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Abilities(1)
    test2 = Abilities(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("effect_changes[0].effect_entries[0].effect", "Hat im Kampf keinen Effekt."),
    ("effect_changes[0].effect_entries[0].language.name", "de"),
    ("effect_changes[0].effect_entries[0].language.url", "https://pokeapi.co/api/v2/language/6/"),
    ("effect_changes[0].version_group.name", "black-white"),
    ("effect_changes[0].version_group.url", "https://pokeapi.co/api/v2/version-group/11/"),
    ("effect_entries[0].effect", "Attacken die Schaden verursachen haben mit jedem Treffer eine 10% Chance das Ziel zur\u00fcckschrecken zu lassen, wenn die Attacke dies nicht bereits als Nebeneffekt hat.\n\nDer Effekt stapelt nicht mit dem von getragenen Items.\n\nAu\u00dferhalb vom Kampf: Wenn ein Pok\u00e9mon mit dieser F\u00e4higkeit an erster Stelle im Team steht, tauchen wilde Pok\u00e9mon nur halb so oft auf."),
    ("effect_entries[0].language.name", "de"),
    ("effect_entries[0].language.url", "https://pokeapi.co/api/v2/language/6/"),
    ("effect_entries[0].short_effect", "Mit jedem Treffer besteht eine 10% Chance das Ziel zur\u00fcckschrecken zu lassen."),
    ("flavor_text_entries[0].flavor_text", "Helps repel wild POK\u00e9MON."),
    ("flavor_text_entries[0].language.name", "en"),
    ("flavor_text_entries[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("flavor_text_entries[0].version_group.name", "ruby-sapphire"),
    ("flavor_text_entries[0].version_group.url", "https://pokeapi.co/api/v2/version-group/5/"),
    ("generation.name", "generation-iii"),
    ("generation.url", "https://pokeapi.co/api/v2/generation/3/"),
    ("id", 1),
    ("is_main_series", True),
    ("name", "stench"),
    ("names[0].language.name", "fr"),
    ("names[0].language.url", "https://pokeapi.co/api/v2/language/5/"),
    ("names[0].name", "Puanteur"),
    ("pokemon[0].is_hidden", True),
    ("pokemon[0].slot", 3),
    ("pokemon[0].pokemon.name", "gloom"),
    ("pokemon[0].pokemon.url", "https://pokeapi.co/api/v2/pokemon/44/"),
    
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Abilities(1)
    
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