import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN =  'a86ac26cf56cbfb174f1f325c625e9a8'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

body_change = {
    "pokemon_id": "290351",
    "name": "Bulba",
    "photo_id": 2
}

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

body_addpockeball = {
    "pokemon_id": "290351"
}

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpockeball)
print(response_addpokeball.text)