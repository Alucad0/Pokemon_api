import requests
import random

# creates a random pokémon based on rng
pokemon_number = random.randint(1, 898)
# opens the api url for the randomly created pokémon
link = str("https://pokeapi.co/api/v2/pokemon/{}/").format(pokemon_number)
response = requests.get(link)
response = response.json()
type = response['types'][0]['type']['name']
name = response['name']
abilities = []
hAbilities = []

# goes through all the abilities that the pokémon have
for ability in response['abilities']:
    if ability['is_hidden'] == True:
        hAbilities.append(ability['ability']['name'])
    else:
        abilities.append(ability['ability']['name'])


print (abilities, hAbilities)
