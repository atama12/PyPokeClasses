import pytest
from unittest.mock import patch
from PyPokeClasses.Moves import Moves
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Move/files/move.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = Moves(1)
    test2 = Moves(50000)

    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("accuracy",100),
    ("contest_combos.normal.use_after[0].name","aaa1"),
    ("contest_combos.normal.use_after[0].url","bbb1"),
    ("contest_combos.normal.use_before[0].name","double-slap"),
    ("contest_combos.normal.use_before[0].url","https://pokeapi.co/api/v2/move/3/"),
    ("contest_combos.super.use_after[0].name","aaa2"),
    ("contest_combos.super.use_after[0].url","bbb2"),
    ("contest_combos.super.use_before[0].name","aaa3"),
    ("contest_combos.super.use_before[0].url","bbb3"),
    ("contest_effect.url","https://pokeapi.co/api/v2/contest-effect/1/"),
    ("contest_type.name","tough"),
    ("contest_type.url","https://pokeapi.co/api/v2/contest-type/5/"),
    ("damage_class.name","physical"),
    ("damage_class.url","https://pokeapi.co/api/v2/move-damage-class/2/"),
    ("effect_chance",0),
    ("effect_changes[0].effect_entries[0].effect","efe_aaa"),
    ("effect_changes[0].effect_entries[0].language.name","la_aaaa"),
    ("effect_changes[0].effect_entries[0].language.url","la_bbbb"),
    ("effect_changes[0].version_group.name","vg_aaaa"),
    ("effect_changes[0].version_group.url","vg_bbbb"),
    ("effect_entries[0].effect","Inflicts regular damage."),
    ("effect_entries[0].language.name","en"),
    ("effect_entries[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("effect_entries[0].short_effect","Inflicts regular damage with no additional effect."),
    ("flavor_text_entries[0].flavor_text","Pounds with fore\u00ad\nlegs or tail."),
    ("flavor_text_entries[0].language.name","en"),
    ("flavor_text_entries[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("flavor_text_entries[0].version_group.name","gold-silver"),
    ("flavor_text_entries[0].version_group.url","https://pokeapi.co/api/v2/version-group/3/"),
    ("generation.name","generation-i"),
    ("generation.url","https://pokeapi.co/api/v2/generation/1/"),
    ("id",1),
    ("learned_by_pokemon[0].name","clefairy"),
    ("learned_by_pokemon[0].url","https://pokeapi.co/api/v2/pokemon/35/"),
    ("machines[0].machine.url","machine_aaa"),
    ("machines[0].version_group.name","vg_aaa"),
    ("machines[0].version_group.url","vg_bbb"),
    ("meta.ailment.name","none"),
    ("meta.ailment.url","https://pokeapi.co/api/v2/move-ailment/0/"),
    ("meta.ailment_chance",0),
    ("meta.category.name","damage"),
    ("meta.category.url","https://pokeapi.co/api/v2/move-category/0/"),
    ("meta.crit_rate",0),
    ("meta.drain",0),
    ("meta.flinch_chance",0),
    ("meta.healing",0),
    ("meta.max_hits",0),
    ("meta.min_hits",0),
    ("meta.min_turns",0),
    ("meta.stat_chance",0),
    ("name","pound"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","\u306f\u305f\u304f"),
    ("past_values[0].accuracy",1),
    ("past_values[0].effect_chance",0),
    ("past_values[0].power",1),
    ("past_values[0].pp",10),
    ("past_values[0].effect_entries[0].effect","effe"),
    ("past_values[0].effect_entries[0].short_effect","short effe"),
    ("past_values[0].effect_entries[0].language.name","la"),
    ("past_values[0].effect_entries[0].language.url","lala"),
    ("past_values[0].type.name","aaa"),
    ("past_values[0].type.url","bbb"),
    ("past_values[0].version_group.name","aaa"),
    ("past_values[0].version_group.url","bbb"),
    ("power",40),
    ("pp",35),
    ("priority",0),
    ("stat_changes[0].change",100),
    ("stat_changes[0].stat.name","stat_aaa"),
    ("stat_changes[0].stat.url","stat_bbb"),
    ("super_contest_effect.url","https://pokeapi.co/api/v2/super-contest-effect/5/"),
    ("target.name","selected-pokemon"),
    ("target.url","https://pokeapi.co/api/v2/move-target/10/"),
    ("type.name","normal"),
    ("type.url","https://pokeapi.co/api/v2/type/1/"),
    
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = Moves(1)
    
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