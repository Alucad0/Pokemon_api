import requests
import random
from pokemon_class import *

# creates a random pokémon based on rng
mon_numb = random.randint(1, 898)
# opens the api url for the randomly created pokémon
link = str("https://pokeapi.co/api/v2/pokemon/{}/").format(mon_numb)
response = requests.get(link)
response = response.json()

# variables:
mon_numb = mon_numb
mon_name = response['name']
sprite = response['sprites']['front_default']
mon_type = []
abi = []
gen = int

# goes throgh all of the typings the pokémon has and adds them to the list
for type in response['types']:
    mon_type.append(type['type']['name'])

# goes through all of the abilities that the pokémon could have and adds them to the list
for ability in response['abilities']:
    abi.append(ability['ability']['name'])

# hardcoded a bruteforce for the generation
if mon_numb<152:
    gen = 1
elif mon_numb>151 and mon_numb<252:
    gen = 2
elif mon_numb>251 and mon_numb<387:
    gen = 3
elif mon_numb>386 and mon_numb<494:
    gen = 4
elif mon_numb>493 and mon_numb<650:
    gen = 5
elif mon_numb>649 and mon_numb<722:
    gen = 6
elif mon_numb>721 and mon_numb<810:
    gen = 7
elif mon_numb>809 and mon_numb<899:
    gen = 8


mon = Pokemon(mon_name, mon_numb, mon_type, abi, gen, sprite)
