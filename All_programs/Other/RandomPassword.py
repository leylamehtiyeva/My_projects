"""Класс RandomPassword для генерации случайных паролей"""

from random import randint

class RandomPassword:
    #psw_chars - строка из разрешенных в пароле символов;
    # min_length, max_length - минимальная и максимальная длина генерируемых паролей.
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw = psw_chars
        self.__minl = min_length
        self.__maxl = max_length

    def __call__(self, *args, **kwargs):
        length = randint(self.__minl, self.__maxl)
        len_chars = len(self.__psw)
        return "".join(self.__psw[randint(0, len_chars-1)] for _ in range(length))



min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(2)]



