class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        self.__total_attrs = len(kwargs)
        self.keys = tuple(self.__dict__.keys())

    def __check_index(self, indx):
        if type(indx) != int or not -self.__total_attrs <= indx < self.__total_attrs:
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self.keys[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self.keys[key], value)


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r[0.5])
