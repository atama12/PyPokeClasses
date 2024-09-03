import pytest
from unittest.mock import patch
from pokeAPI_Models.Pokemon import *  # 実際のモジュール名に変更

class TestPokemon:
    
    @patch('my_pokeapi_module.requests.get')
    def test_pokemon_init(self, mock_get):
        # モックレスポンスの設定
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "name": "pikachu",
            "height": 4,
            "weight": 60,
            "abilities": [
                {"ability": {"name": "static", "url": "https://pokeapi.co/api/v2/ability/9/"}},
                {"ability": {"name": "lightning-rod", "url": "https://pokeapi.co/api/v2/ability/31/"}}
            ]
        }

        # インスタンス生成とテスト
        pikachu = Pokemon('pikachu')
        assert pikachu.name == "pikachu"
        assert pikachu.height == 4
        assert pikachu.weight == 60
        assert len(pikachu.abilities) == 2

    @patch('my_pokeapi_module.requests.get')
    def test_pokemon_404(self, mock_get):
        # 404レスポンスの設定
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = None

        # インスタンス生成とテスト
        unknown_pokemon = Pokemon('unknown_pokemon')
        assert unknown_pokemon.name is None
        assert unknown_pokemon.height is None
        assert unknown_pokemon.weight is None