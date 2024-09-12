import pytest
from unittest.mock import patch
from PyPokeClasses.Evolution import EvolutionChain
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Evolution/files/evolution-chain.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = EvolutionChain(1)
    test2 = EvolutionChain(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("id",1),
    ("baby_trigger_item.name","aaa"),
    ("baby_trigger_item.url","bbb"),
    ("chain.evolution_details[0].gender",1),
    ("chain.evolution_details[0].held_item.name","aaa2"),
    ("chain.evolution_details[0].held_item.url","bbb2"),
    ("chain.evolution_details[0].item.name","aaa3"),
    ("chain.evolution_details[0].item.url","bbb3"),
    ("chain.evolution_details[0].known_move.name","aaa4"),
    ("chain.evolution_details[0].known_move.url","bbb4"),
    ("chain.evolution_details[0].known_move_type.name","aaa5"),
    ("chain.evolution_details[0].known_move_type.url","bbb5"),
    ("chain.evolution_details[0].location.name","aaa6"),
    ("chain.evolution_details[0].location.url","bbb6"),
    ("chain.evolution_details[0].min_affection",1),
    ("chain.evolution_details[0].min_beauty",2),
    ("chain.evolution_details[0].min_happiness",2),
    ("chain.evolution_details[0].min_level",16),
    ("chain.evolution_details[0].needs_overworld_rain",False),
    ("chain.evolution_details[0].party_species.name","aaa7"),
    ("chain.evolution_details[0].party_species.url","bbb7"),
    ("chain.evolution_details[0].party_type.name","aaa8"),
    ("chain.evolution_details[0].party_type.url","bbb8"),
    ("chain.evolution_details[0].relative_physical_stats",3),
    ("chain.evolution_details[0].time_of_day","ccc"),
    ("chain.evolution_details[0].trade_species.name","aaa9"),
    ("chain.evolution_details[0].trade_species.url","bbb9"),
    ("chain.evolution_details[0].trigger.name","level-up"),
    ("chain.evolution_details[0].trigger.url","https://pokeapi.co/api/v2/evolution-trigger/1/"),
    ("chain.evolution_details[0].turn_upside_down",False),
    
    ("chain.is_baby",False),
    ("chain.species.name","bulbasaur"),
    ("chain.species.url","https://pokeapi.co/api/v2/pokemon-species/1/"),
    
    ("chain.evolves_to[0].evolution_details[0].gender",1),
    ("chain.evolves_to[0].evolution_details[0].held_item.name","aaa2"),
    ("chain.evolves_to[0].evolution_details[0].held_item.url","bbb2"),
    ("chain.evolves_to[0].evolution_details[0].item.name","aaa3"),
    ("chain.evolves_to[0].evolution_details[0].item.url","bbb3"),
    ("chain.evolves_to[0].evolution_details[0].known_move.name","aaa4"),
    ("chain.evolves_to[0].evolution_details[0].known_move.url","bbb4"),
    ("chain.evolves_to[0].evolution_details[0].known_move_type.name","aaa5"),
    ("chain.evolves_to[0].evolution_details[0].known_move_type.url","bbb5"),
    ("chain.evolves_to[0].evolution_details[0].location.name","aaa6"),
    ("chain.evolves_to[0].evolution_details[0].location.url","bbb6"),
    ("chain.evolves_to[0].evolution_details[0].min_affection",1),
    ("chain.evolves_to[0].evolution_details[0].min_beauty",2),
    ("chain.evolves_to[0].evolution_details[0].min_happiness",2),
    ("chain.evolves_to[0].evolution_details[0].min_level",16),
    ("chain.evolves_to[0].evolution_details[0].needs_overworld_rain",False),
    ("chain.evolves_to[0].evolution_details[0].party_species.name","aaa7"),
    ("chain.evolves_to[0].evolution_details[0].party_species.url","bbb7"),
    ("chain.evolves_to[0].evolution_details[0].party_type.name","aaa8"),
    ("chain.evolves_to[0].evolution_details[0].party_type.url","bbb8"),
    ("chain.evolves_to[0].evolution_details[0].relative_physical_stats",3),
    ("chain.evolves_to[0].evolution_details[0].time_of_day","ccc"),
    ("chain.evolves_to[0].evolution_details[0].trade_species.name","aaa9"),
    ("chain.evolves_to[0].evolution_details[0].trade_species.url","bbb9"),
    ("chain.evolves_to[0].evolution_details[0].trigger.name","level-up"),
    ("chain.evolves_to[0].evolution_details[0].trigger.url","https://pokeapi.co/api/v2/evolution-trigger/1/"),
    ("chain.evolves_to[0].evolution_details[0].turn_upside_down",False),
    
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].gender",1),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].held_item.name","aaa2"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].held_item.url","bbb2"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].item.name","aaa3"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].item.url","bbb3"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].known_move.name","aaa4"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].known_move.url","bbb4"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].known_move_type.name","aaa5"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].known_move_type.url","bbb5"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].location.name","aaa6"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].location.url","bbb6"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].min_affection",1),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].min_beauty",2),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].min_happiness",2),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].min_level",32),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].needs_overworld_rain",False),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].party_species.name","aaa7"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].party_species.url","bbb7"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].party_type.name","aaa8"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].party_type.url","bbb8"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].relative_physical_stats",3),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].time_of_day","ccc"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].trade_species.name","aaa9"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].trade_species.url","bbb9"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].trigger.name","level-up"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].trigger.url","https://pokeapi.co/api/v2/evolution-trigger/1/"),
    ("chain.evolves_to[0].evolves_to[0].evolution_details[0].turn_upside_down",False),    
    ("chain.evolves_to[0].is_baby",False),
    ("chain.evolves_to[0].species.name","ivysaur"),
    ("chain.evolves_to[0].species.url","https://pokeapi.co/api/v2/pokemon-species/2/"),
    
])
@patch('PyPokeClasses.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = EvolutionChain(1)
    
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