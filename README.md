# Pokemon_api

## Table of contents

- Destription of the project
- Requirements
- Installation
- Issuetracker
- Code conventions
- API
- Example/Test run
- Contribution
- Contributors
- Contact
- Changelog

### Descrption of the project

This project is going to be a fully automated pokemon guessing game. 
All of the information required for the game will be taken from the pokemon api. 
The program will start by asking the user if they wanna play (input = str yes or no). 
If the answer is yes, that they wanna play, then the first round will begin with round (round = 1). 
The user is going to be guessing "who is that pokemon?" (while they wanna play) and successively get more and more clues with each incorect guess until there are no more clues to be given (counting up with each loop and clues will be given depending on the counter). 
Thereupon, after all the clues have been shown, the user will have 2 remaining guesses (if count = x then game over). 
After the user has either guess wrong or incorrectly too many times the round will end and it will ask the user wether they wanna continue playing or quit (input = quit or play). 
If the user decides to continue playing then the round counter will increase (round += 1). 

### Requirements

- Python.
- request module.
- random module.

### Installation

Pokemon_api is was made with __Python 3.7+__. You can download the latest version of Python [here](https://www.python.org/downloads/).

The three packages (random, requests & webbrowser) can be install your IDE (Intergrated Developer Enviroment). 
Note that each IDE has a different way to install packages. 
Otherwise you can use the your command prompt and changing the directory to where Python is installd and into the scripts folder. 
There type `pip install requests`, `pip install random` and `pip install webbrowser`

### Issuetracker/Opportunities for improvement

The current program does not have graphical interface which would have been prefered. Instead it uses the webbrowser packages to show the sprite of the pokemon. This is something that is currently being developed.

### Code conventions

**File organisation:** The code is divided into different files, by order of functions, for easier interaction and to facilitate contributions.

**Naming convention:** All the files use **snake_case** for variable names.

**Comments:** One-line comments are written above the code line to explain the code and its purpose. The same principle applies to block comments.

### API

![Pokémon_UML drawio](https://user-images.githubusercontent.com/96413210/154013332-48de409a-54ae-4139-9fb3-5d4a93bc90a4.png)

All of the methods return a specific variable. 

### Example/Testrun

```powershell
This is "Guess that Pokémon!"


Round 1
Name: _ _ _ _ _ _ _ _ _      
Generation: 7
Ability: ['swarm', 'rivalry']

Who is that Pokemon:  pikachu


Round 2
Name: B _ _ _ _ _ _ _ _ 
Generation: 7
Ability: ['swarm', 'rivalry']
Type: ['bug', 'flying']
Index: 267
Previous guesses: ['pikachu']

Who's that Pokemon:  beedrill


Round 3
Name: B _ _ _ _ _ _ _ _
Generation: 7
Ability: ['swarm', 'rivalry']
Type: ['bug', 'flying']
Index: 267
Previous guesses: ['pikachu', 'beedrill']

Who is that Pokemon:  Beautifly 
That is right, the pokémon was beautifly
Do you wish to continue playing:  no

```

### Contribution

This is a school project and it will get an failing grade if anyone contributes majorly, so any pull requests will be denied after it has been graded. 

Feel free to contribute to this code after the grade has been set (after 27/2 - 2022). 
For major changes, please open an issue first to discuss what you would like to change. 
Please make a comment about what is changing. 

### Contributors

- [NurarihyonMaou](https://github.com/NurarihyonMaou)
- [Bern4rdR](https://github.com/Bern4rdR)
- [nilund93](https://github.com/Nilund93)

### Contact

- Author: Fredrik M (Alucad0)
  - Discord: Alucado#3986
  - E-mail: fredrik.magnevill@gmail.com
  - Phonenumber: +46 073 373 40 05
    - If you want you can use swish to pay me.

### Changelog

This changelog will only updated after major changes and it will begin with the complete version of this project (after 27/2 - 2022).

## License

[MIT](https://choosealicense.com/licenses/mit/)
