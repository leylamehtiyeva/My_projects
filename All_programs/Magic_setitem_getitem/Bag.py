class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []
        self.summary_weight = 0

    def __check_weight(self, new_thing, old_thing=None):
        res = self.summary_weight + new_thing.weight if old_thing is None \
            else self.summary_weight + new_thing.weight - old_thing.weight
        if res > self.max_weight:
            raise ValueError('Total weight of items exceeded')

    def add_thing(self, thing):
        self.__check_weight(thing)
        self.bag.append(thing)
        self.summary_weight += thing.weight

    def __check_index(self, item):
        if not (0 <= item < len(self.bag)):
            raise IndexError('invalid index')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        t = self.bag[key]
        self.__check_weight(value, t)
        self.bag[key] = value
        self.summary_weight += (value.weight - t.weight)

    def __delitem__(self, key):
        self.__check_index(key)
        res = self.bag.pop(key)
        self.summary_weight -= res.weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
"""print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4]"""