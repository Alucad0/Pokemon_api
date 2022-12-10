class Pokemon():
    def __init__(self, name, pokedex_index, type, ability, generation, sprite):
        self.name = name
        self.numb = pokedex_index
        self.type = type
        self.ability = ability
        self.gen = generation
        self.png = sprite

    def get_name(self):
        return self.name

    def get_numb(self):
        return self.numb

    def get_type(self):
        ret_string = self.type.replace("  ", ", ")
        return ret_string

    def get_ability(self):
        ret_string = self.ability.replace("  ", ", ")
        return ret_string

    def get_gen(self):
        return self.gen

    def get_sprite(self):
        return self.png
