import requests
import random

# creates a random pokemon based on rng
pokemon_number = random.randint(1, 898)

link = str("https://pokeapi.co/api/v2/pokemon/{}/").format(pokemon_number)
response = requests.get(link)
response = response.json()
type = response['types'][0]['type']['name']
name = response['name']
abilities = []
hAbilities = []


for ability in response['abilities']:
    if ability['is_hidden'] == True:
        hAbilities.append(ability['ability']['name'])
    else:
        abilities.append(ability['ability']['name'])


print (abilities, hAbilities)
