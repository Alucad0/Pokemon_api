import requests
import random

from pokemon_class import Pokemon

# creates a random pokémon based on rng
mon_numb = random.randint(1, 898)
# opens the api url for the randomly created pokémon
link = str("https://pokeapi.co/api/v2/pokemon/{}/").format(mon_numb)
response = requests.get(link)
response = response.json()

mon_type = []
mon_type.append(response['types'][0]['type']['name'])
# needs to add if it got a second type, like butterfly got bug and flying. Does it already do that?

# generation number - can be brute forced

# png or gif of the sprite 
# example of the link from the api that I wanna get
    # https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/female/267.gif

# rarity value 

mon_name = response['name']
# only wanna have the primary ability
abi = []
hid_abi = []

# goes through all the abilities that the pokémon have
for ability in response['abilities']:
    if ability['is_hidden'] == True:
        hid_abi.append(ability['ability']['name'])
    else:
        abi.append(ability['ability']['name'])


print(mon_type)
mon = Pokemon(mon_name, mon_numb, mon_type, abi, hid_abi)
