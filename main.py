import requests
import random
from pokemon_class import *

def game():
    # creates a random pokémon based on rng
    mon_numb = random.randint(1, 898)
    # opens the api url for the randomly created pokémon
    link = str(f"https://pokeapi.co/api/v2/pokemon/{mon_numb}/")
    response = requests.get(link)
    response = response.json()

    # variables:
    round = 1
    playing = True
    prev_guess = []
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
    if mon_numb<152: gen = 1
    elif mon_numb>151 and mon_numb<252: gen = 2
    elif mon_numb>251 and mon_numb<387: gen = 3
    elif mon_numb>386 and mon_numb<494: gen = 4
    elif mon_numb>493 and mon_numb<650: gen = 5
    elif mon_numb>649 and mon_numb<722: gen = 6
    elif mon_numb>721 and mon_numb<810: gen = 7
    elif mon_numb>809 and mon_numb<899: gen = 8


    mon = Pokemon(mon_name, mon_numb, mon_type, abi, gen, sprite)

    # starting the looping terminal game
    print('This is "Guess that Pokémon!"\n')
    while playing:
        print(f"Round {round}")
        
        # the clues will be re-printed for each round with more clues depending on the round.
        if round >= 1:
            format_name = "_ " # * len(ret_name)
            print(f"Name: {format_name}")
            print(f"Generation: {}") # mon.ret_gen()
            print(f"Ability: {}") # mon.ret_ability()
        
        if round >= 2:
            # format_name = mon.ret_name()[0] + " -" * len(ret_name - 1)
            print(f"Type: {}") # mon.ret_type()
            print(f"Index: {}") # mon.ret_index()

        if round >= 3:
            # sprite
            pass


        guess = str(input("Who's that Pokemon:  "))
        prev_guess.append(guess.lower())

        if guess.lower() == #mon.ret_name.lower():
            print(f"Thats right, the pokémon was {}") #mon.ret_name()
            cont = str(input("Do you wish to continue playing:  "))
            if cont in ["yes", "yeas", "y", "ye", "yeah", "continue", "c", "cont"]:
                game()        

        if round == 5:
            print("You lost")
            cont = str(input("Do you wish to continue playing:  "))
            if cont in ["yes", "yeas", "y", "ye", "yeah", "continue", "c", "cont"]:
                game()

        round += 1




play = str(input("Do you wanna play:    "))

if play in ["yes", "yeas", "y", "ye"]:
    game()
