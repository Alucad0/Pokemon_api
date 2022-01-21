class Pokemon():
    def __init__(self, name, pokedex_index, typings, ability, hidden_ability):
        self.name = name
        self.numb = pokedex_index
        self.type = typings
        self.ability = ability
        self.hid_ability = hidden_ability
    
    # create functions that reveal all info - one part at time
