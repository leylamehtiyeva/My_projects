"""Здесь в каждом узле дерева делается проверка (задается вопрос). Если проверка проходит,
то осуществляется переход к следующему объекту по левой стрелке (с единицей),
а иначе - по правой стрелке (с нулем). И так до тех пор, пока не дойдем до одного из листа дерева
(вершины без потомков).В качестве входных данных используется вектор (список) с
бинарными значениями: 1 - да, 0 - нет"""


'''Далее, этот вектор применяется к решающему дереву, следующим образом. 
Корневая вершина "Любит Python" с ней связан первый элемент вектора x и содержит значение 1, 
следовательно, мы переходим по левой ветви. Попадаем в вершину "Понимает ООП". 
С ней связан второй элемент вектора x со значением 0, следовательно, мы переходим по правой ветви и 
попадаем в вершину "будет кодером". Так как эта вершина конечная (листовая), 
то получаем результат в виде строки "будет кодером". По аналогии выполняется обработка вектора x с 
другими наборами значений 0 и 1.
'''



class TreeObj:
    def __init__(self, indx, value=None):
        self.index = indx
        self.value = value
        self.__left = self.__right = None


    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            else:
                obj = obj_next
        return obj.value


    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        else:
            return obj.right

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом

print(res)