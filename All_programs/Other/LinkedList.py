class ObjList:
    def __init__(self, data):
        self.__data = ""
        self.__prev =  self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if obj in (ObjList, None):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if obj in (ObjList, None):
            self.__next = obj








class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if not self.head:
            self.head = obj

    def __get_obj_by_indx(indx):


    def remove_obj(self, indx):
        obj = self.__get_obj_by_indx(indx)



