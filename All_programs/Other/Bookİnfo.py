"""Объявите класс Book для представления информации о книге."""

class Book:
    attrs_type = {'title': str, 'author': str, 'pages': int, 'year': int }

    def __init__(self, title = '', author = '', pages = 0, year = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.attrs_type and self.attrs_type[key] == type(value):
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', "Сергей Балакирев", 123, 2022)
print(book)