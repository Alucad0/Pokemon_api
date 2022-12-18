import requests
import random
import webbrowser
from pokemon_class import *

def create_pokemon(mon_numb):
      # opens the api url for the randomly created pokémon
      link = str(f"https://pokeapi.co/api/v2/pokemon/{mon_numb}/")
      response = requests.get(link)
      response = response.json()
      mon_name = response['name']
      sprite = response['sprites']['front_default']
      mon_type = str()
      abi = str()
      gen = int

      # goes throgh all of the typings the pokémon has and adds them to the string
      for type in response['types']:
            mon_type += f" {type['type']['name']} "

      # goes through all of the abilities that the pokémon could have and adds them to a string
      for ability in response['abilities']:
            abi += f" {ability['ability']['name']} "

      # hardcoded a bruteforce for the generation
      if mon_numb<152: gen = 1
      elif mon_numb>151 and mon_numb<252: gen = 2
      elif mon_numb>251 and mon_numb<387: gen = 3
      elif mon_numb>386 and mon_numb<494: gen = 4
      elif mon_numb>493 and mon_numb<650: gen = 5
      elif mon_numb>649 and mon_numb<722: gen = 6
      elif mon_numb>721 and mon_numb<810: gen = 7
      elif mon_numb>809 and mon_numb<899: gen = 8

      return Pokemon(mon_name, mon_numb, mon_type, abi, gen, sprite)


def game():
    # creates a random pokémon based on rng
    index = random.randint(1, 898)
   
    # variables:
    round = 1
    playing = True
    prev_guess = str()
    mon = create_pokemon(index)
   
    format_name = "_ " * len(mon.get_name())

    # starting the looping terminal game
    while playing:
        print(f"\n\nRound {round}")

        # each round represents a set of clues and the clues will add up and change with each incorecct guess
        # the clues will be re-printed for each round with more clues depending on the round.
        if round >= 1:
            print(f"Name: {format_name}")
            print(f"Generation: {mon.get_gen()}") 
            print(f"Ability: {mon.get_ability()}")
            format_name = mon.get_name()[0].capitalize() + " -" * (len(mon.get_name()) - 1) 
        
        if round >= 2:
            print(f"Type: {mon.get_type()}") 
            print(f"Index: {mon.get_numb()}")
            print(f"Previous guesses:{prev_guess}")

        if round == 3:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(mon.get_sprite())
        
        guess = str(input("\nWho's that Pokemon:  ")).lower()
        prev_guess += f" {guess}."
        if round > 1:
            prev_guess = prev_guess[:-1].replace(".", ",") + "."

        if guess == mon.ret_name():
            print(f"Thats right, the pokémon was {mon.get_name().capitalize()}") 
            cont = str(input("Do you wish to continue playing:  "))
            if cont.lower() in ["yes", "yeas", "y", "ye", "yeah", "continue", "c", "cont"]:
                game()        
            else:
                break

        if round == 5:
            print(f"You lost. The pokémon was {mon.get_name().capitalize()}")
            cont = str(input("Do you wish to continue playing:  "))
            if cont.lower() in ["yes", "yeas", "y", "ye", "yeah", "continue", "c", "cont"]:
                game()
            else:
                break
        round += 1


def main():
      play = str(input("Do you wanna play:    "))

      if play.lower() in ["yes", "yeas", "y", "ye"]:
            print('This is "Guess that Pokémon!"')
            game()

      else: 
            print("Okey, then go fuck yourself - why did you even start the program?")


main()
