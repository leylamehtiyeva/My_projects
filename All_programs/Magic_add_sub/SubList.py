class NewList:
    def __init__(self, lst=None):
        self.lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self.lst

    @staticmethod
    def __diff_list(lst_1,lst_2):
        if len(lst_2) == 0:
            return lst_1

        sub = lst_2[:]
        return [x for x in lst_1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        """
        Check weather element x is included in the list sub
        :param x: element of list
        :param sub: list
        :return: True if for some element of the list sub passes the condition else return False
        This means that value 'x' is included in the list of sub
        """
        # here we check bool True/False and int 0/1
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res #True/False



    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError('Error')
        return NewList(self.__diff_list(other, self.lst))



    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError('Error')
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self.lst, other_list))

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]




