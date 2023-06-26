class PhoneBook:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)


    def remove_phone(self, indx):
        self.phones.pop(indx)

    def get_phone_list(self):
        return self.phones


class PhoneNumber:
    def __init__(self, number, fio):
        if type(number) == int and len(str(number))==11:
            self.number = number
        if type(fio) == str:
            self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)


