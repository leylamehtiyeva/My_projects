class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

lst = [stroka.split(': ') for stroka in lst]
lst1 = [[lst_in[0], *lst_in[-1].split()] for lst_in in lst]
res = [ShopItem(*lst) for lst in lst1]
print(res)