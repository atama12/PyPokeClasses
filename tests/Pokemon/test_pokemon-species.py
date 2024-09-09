import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import PokemonSpecies
import json

# 1. モックデータをファイルから読み込むためのfixture
@pytest.fixture
def mock_response_data():
    with open('tests/Pokemon/files/pokemon-species.json', 'r') as file:
        return json.load(file)


# 2. API問い合わせのステータスコードが200であることを確認するテスト
def test_api_connect():

    test1 = PokemonSpecies(1)
    test2 = PokemonSpecies(50000)
    # ステータスコードが200であることを確認
    assert test1.status_code == 200
    assert test2.status_code == 404

# 3. JSONデータのプロパティが正しく定義されていることを確認するテスト
@pytest.mark.parametrize("property_name, expected_value", [
    ("base_happiness",50),
    ("capture_rate",45),
    ("color.name","green"),
    ("color.url","https://pokeapi.co/api/v2/pokemon-color/5/"),
    ("egg_groups[0].name","monster"),
    ("egg_groups[0].url","https://pokeapi.co/api/v2/egg-group/1/"),
    ("evolution_chain.url","https://pokeapi.co/api/v2/evolution-chain/1/"),
    ("evolves_from_species",None),
    ("flavor_text_entries[0].flavor_text","A strange seed was\nplanted on its\nback at birth.\fThe plant sprouts\nand grows with\nthis POK\u00e9MON."),
    ("flavor_text_entries[0].language.name","en"),
    ("flavor_text_entries[0].language.url","https://pokeapi.co/api/v2/language/9/"),
    ("flavor_text_entries[0].version.name","red"),
    ("flavor_text_entries[0].version.url","https://pokeapi.co/api/v2/version/1/"),
    ("form_descriptions",[]),
    ("forms_switchable",False),
    ("gender_rate",1),
    ("genera[0].genus","\u305f\u306d\u30dd\u30b1\u30e2\u30f3"),
    ("genera[0].language.name","ja-Hrkt"),
    ("genera[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("generation.name","generation-i"),
    ("generation.url","https://pokeapi.co/api/v2/generation/1/"),
    ("growth_rate.name","medium-slow"),
    ("growth_rate.url","https://pokeapi.co/api/v2/growth-rate/4/"),
    ("habitat.name","grassland"),
    ("habitat.url","https://pokeapi.co/api/v2/pokemon-habitat/3/"),
    ("has_gender_differences",False),
    ("hatch_counter",20),
    ("id",1),
    ("is_baby",False),
    ("is_legendary",False),
    ("is_mythical",False),
    ("name","bulbasaur"),
    ("names[0].language.name","ja-Hrkt"),
    ("names[0].language.url","https://pokeapi.co/api/v2/language/1/"),
    ("names[0].name","\u30d5\u30b7\u30ae\u30c0\u30cd"),
    ("order",1),
    ("pal_park_encounters[0].area.name","field"),
    ("pal_park_encounters[0].area.url","https://pokeapi.co/api/v2/pal-park-area/2/"),
    ("pal_park_encounters[0].base_score",50),
    ("pal_park_encounters[0].rate",30),
    ("pokedex_numbers[0].entry_number",1),
    ("pokedex_numbers[0].pokedex.name","national"),
    ("pokedex_numbers[0].pokedex.url","https://pokeapi.co/api/v2/pokedex/1/"),
    ("shape.name","quadruped"),
    ("shape.url","https://pokeapi.co/api/v2/pokemon-shape/8/"),
    ("varieties[0].is_default",True),
    ("varieties[0].pokemon.name","bulbasaur"),
    ("varieties[0].pokemon.url","https://pokeapi.co/api/v2/pokemon/1/"),
])
@patch('pokeAPI_Models.Utility.Common.BaseModel.make_request')

def test_data_check(mock_make_request, property_name, expected_value, mock_response_data):
    mock_make_request.return_value = (mock_response_data)

    test_data = PokemonSpecies(1)
    
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