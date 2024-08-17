from Models.Pokemon import Pokemon

# ポケモンデータを格納するリスト
extracted_data = []

data = Pokemon(2)
data2 = data.abilities
print(data.moves)
# ポケモンデータの取得とリストへの追加
#for i in range(1):
    
#     data = session.get("https://pokeapi.co/api/v2/pokemon/"+ str(i+1))
#     species_data = session.get("https://pokeapi.co/api/v2/pokemon-species/" + str(i+1))
    
#     # レスポンスが成功しているか確認
#     if data.status_code == 200 and species_data.status_code == 200:
#         json_data:dict = data.json()  # JSONデータを取得
#         species_json:dict = species_data.json()
#     else:
#         print(f"Failed to retrieve data: {data.status_code}")
#         print(f"Failed to retrieve data: {species_data.status_code}")
#         json_data = None
#         species_json = None

#     # 2. 必要なキーを抽出
#     if json_data and species_json:
        
#         extracted_data.append({
#             "id": json_data.get("id"),
#             "name": species_json["names"][0]["name"],
#             "class_name": species_json["genera"][0]["genus"],
#             "first_generation": species_json["genera"][0]["genus"],
#             "icon":json_data["sprites"]["front_default"],
#             "type_id1":str(json_data["types"][0]["type"]["url"]).split('/')[-2],
#             "type_id2":str(json_data["types"][1]["type"]["url"]).split('/')[-2],
#             "charact_id1":str(json_data["abilities"][0]["ability"]["url"]).split('/')[-2],
#             "charact_id2":str(json_data["abilities"][1]["ability"]["url"]).split('/')[-2],
#             "dream_charact_id":str(json_data["abilities"][1]["ability"]["url"]).split('/')[-2],
#             "egg_gr1":str(species_json["egg_groups"][0]["url"]).split('/')[-2],
#             "egg_gr2":str(species_json["egg_groups"][1]["url"]).split('/')[-2],
#             "evo_chart":str(species_json["evolution_chain"]["url"]).split('/')[-2],
#             "height": json_data.get("height"),
#             "weight": json_data.get("weight"),
#             "voice":json_data["cries"]["latest"]
#         })

# # 3. DataFrameに変換
# df = pd.DataFrame(extracted_data)

# # CSVファイルとして保存
# df.to_csv("pokemon_data.csv", index=False)
