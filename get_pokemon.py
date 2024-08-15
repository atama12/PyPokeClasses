import requests
import json
from Struct.common import Pokemon

# PokeAPIのエンドポイント
url = "https://pokeapi.co/api/v2/pokemon-species/"

# for i in range(10):
#     # 取得したいポケモンの名前またはID
#     pokemon_name_or_id = str(i+1)  # 例: "pikachu" または 25


#     # APIからデータを取得
#     response = requests.get(url + pokemon_name_or_id)

#     # レスポンスが成功したか確認
#     if response.status_code == 200:
#         # JSON形式でデータを取得
#         pokemon_data = response.json()
        
#         # JSONファイルとして保存
#         with open(f"{pokemon_name_or_id}.json", "w") as json_file:
#             json.dump(pokemon_data, json_file, indent=4)
        
#         print(f"{pokemon_name_or_id}.jsonファイルに保存しました。")
#     else:
#         print(f"ポケモン{pokemon_name_or_id}のデータを取得できませんでした。ステータスコード: {response.status_code}")