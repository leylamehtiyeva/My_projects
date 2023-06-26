class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True


    def set_data(self, data):
        self.data = data[:]

    def get_str_data(self):
        return ' '.join(map(str, self.data))

    def show_table(self):
        return ' '.join(self.data)

    def show_graph(self):
        lst = show_table()
        print(f"Графическое отображение данных: {lst}' if self.is_show else "Отображение данных закрыто")

    def show_bar(self):
        lst = show_table()
        print(f"Столбчатая диаграмма: {lst}" if self.is_show else "Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show





