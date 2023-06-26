class Model:
    def __init__(self):
        self.d = {}

    def query(self, **kwargs):
        self.d.update(kwargs)


    def __str__(self):
        if len(self.d) != 0:
            return 'Model: ' + ', '.join([f'{key} = {value}' for key, value in self.d.items()])
        else:
            return 'Model'

model = Model()
model.query(id=1, fio='Sergey', old=33)

print(model)
