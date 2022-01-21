import requests
import random

from pokemon_class import Pokemon

# creates a random pokémon based on rng
mon_numb = random.randint(1, 898)
# opens the api url for the randomly created pokémon
link = str("https://pokeapi.co/api/v2/pokemon/{}/").format(mon_numb)
response = requests.get(link)
response = response.json()
# needs to add if it got a second type, like butterfly got bug and flying. 
mon_type = []
mon_type.append(response['types'][0]['type']['name'])

# rarity value 

mon_name = response['name']
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

"""
It will start with spaces for the name as well as the abilities (all of them)
bad drawing of how the popup window will look
 _______________________________________________________
|                                                       |
|    # XXX     __  __  __  __  __  __  __               | spaces for the name (auto generated based on the name)
|                                                       |
|            ______________________________             |
|           |                              |            | place for the dark siluette of the sprite 
|           |                              |            |
|           |                              |            |
|           |                              |            |
|           |                              |            |
|           |                              |            |
|           |                              |            |
|            ______________________________             |
|                                                       |
|                                                       |
|     Typing:                          Rarity:          |
|                                                       |
|     Ability:                                          |
|                                                       |
|                                                       |
|                Guess:                                 |
|                                                       |
|     Guesses:                                          |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |
|                                                       |

    
"""
