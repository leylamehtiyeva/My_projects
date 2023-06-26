class StringDigit(str):
    def __init__(self, string):
        super().__init__()
        if string.isdigit():
            self.value = string
        else:
            raise ValueError("String must contain only numbers")

    def __add__(self, other):
        res = self.value + other
        if res.isdigit():
            return StringDigit(res)
        else:
            raise ValueError("String must contain only numbers")

    def __radd__(self, other):
        res = other + self.value
        if res.isdigit():
            return StringDigit(res)
        else:
            raise ValueError("String must contain only numbers")


sd2 = StringDigit("123a")

