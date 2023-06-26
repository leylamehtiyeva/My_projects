class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        #converting negative numbers
        if string[0] == '-':
            if string[1:].isdigit():
                return int(string)
        #converting positive numbers
        elif string.isdigit():
                return int(string)
        return None

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)



