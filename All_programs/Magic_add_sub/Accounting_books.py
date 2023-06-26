class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    @staticmethod
    def _verify_value(value):
        if not type(value) == Book:
            raise TypeError('Object must be type Book')

    def __add__(self, other):
        self._verify_value(other)
        if other not in self.book_list:
            self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self._verify_value(other)
        return self + other

    def __sub__(self, other):
        if type(other) == Book and other in self.book_list:
            self.book_list.remove(other)
        elif type(other) == int and other <= len(self.book_list):
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        if type(other) == Book and other in self.book_list:
            return self - other
        elif type(other) == int and other <= len(self.book_list):
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


lib = Lib()
lib = lib + Book('Процесс', 'Кафка', 2020)  # добавление новой книги в библиотеку
lib += Book('Три товарища', 'Ремарк', 2021)
lib += Book('Бесы', 'Достоевский', 2022)
lib += Book('1984', 'Оруэлл', 2022)

lib = lib - Book('Процесс', 'Кафка', 2020)  # удаление книги book из библиотеки
lib -= 9

print(len(lib))


