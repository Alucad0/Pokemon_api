class Pokemon():
    def __init__(self, name, pokedex_index, type, ability, generation, sprite):
        self.name = name
        self.numb = pokedex_index
        self.type = type
        self.ability = ability
        self.gen = generation
        self.png = sprite

    def ret_name(self):
        return self.name

    def ret_numb(self):
        return self.numb

    def ret_type(self):
        ret_string = self.type.replace("  ", ", ")
        return ret_string

    def ret_ability(self):
        ret_string = self.ability.replace("  ", ", ")
        return ret_string

    def ret_gen(self):
        return self.gen

    def ret_sprite(self):
        return self.png
