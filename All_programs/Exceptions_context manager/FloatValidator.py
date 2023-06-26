class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float or not (self.min_value <= value <= self.max_value):
            raise ValueError('Value not validated')


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != int or not (self.min_value <= value <= self.max_value):
            raise ValueError('Value not validated')


def is_valid(lst, validators):
    lst_in = []
    for el in lst:
        for val in validators:
            try:
                val(el)
                lst_in.append(el)
                break
            except:
                pass
    return lst_in

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])
print(lst_out)