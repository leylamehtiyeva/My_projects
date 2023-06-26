class SparseTable:
    def __init__(self):
        self.rows = self.cols = 0
        self.table = {}

    def update_index(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.table[(row, col)]
            self.update_index()
        except KeyError:
            raise IndexError('Cell with specified indexes does not exist')

    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        item = (key[0], key[1])
        if item not in self.table:
            self.table[item] = Cell(value)
            self.update_index()
        else:
            self.table[item] = Cell(value)


class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25  # changing the value of an existing cell
st[11, 7] = 'cell_117'  # creating a new cell
print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - the total number of rows and columns in the table
val = st[2, 5]  # ValueError
st.remove_data(12, 3)  # IndexError
