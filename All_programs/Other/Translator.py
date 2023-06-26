class Translator:


    def add(self, eng, rus):
        if 'my_dict' not in self.__dict__:
            self.my_dict = dict()
        self.my_dict.setdefault(eng, [])
        if rus not in self.my_dict[eng]:
            self.my_dict[eng].append(rus)

    def remove(self, eng):
        if eng in self.my_dict:
            self.my_dict.pop(eng)

    def translate(self, eng):
        return self.my_dict[eng]


tr = Translator()

tr.add("tree", "дерево")
tr.add("tree", "дер")
tr.add("car", "машина")
tr.remove('car')

print(*tr.translate('tree'))

