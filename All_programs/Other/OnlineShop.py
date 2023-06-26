"""Вы создаете интернет-магазин.
Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара."""


class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []


    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)





class Product:
    id_instance = 1
    attrs = {'id': (int, ), 'name': (str, ), 'weight': (int, float), 'price':(int, float)}

    def __init__(self, name, weight, price):
        self.id = Product.id_instance
        Product.id_instance +=1
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) in self.attrs[key]:
            if (key == 'price' or key == 'weight') and value<=0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.attrs:
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)


    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super().__delattr__(item)



shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")





