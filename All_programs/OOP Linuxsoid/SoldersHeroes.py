class Characters:
    character_types = ['solder', 'hero']

    def __init__(self, character_id, character_type):
        if character_type in self.character_types:
            self.character_id = character_id
            self.character_type = character_type
        else:
            raise ValueError('Incorrect input of character type')


class Solders:
    __heroes_list = []

    def follow_the_hero(self, obj):
        self.__heroes_list.append(obj)

    def get_heroes(self):
        return self.__heroes_list


class Heroes:
    level = 0

    def increase_level(self):
        self.level += 1
