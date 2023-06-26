stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


chars = "–?!,.;"
lst = [strochka.strip(chars).replace('  ', ' ').split() for strochka in stich]
print(lst)


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len([slovo for slovo in self.lst_words if slovo.isalpha()])

    def __gt__(self, other):
        return len(self.lst_words) > len(other)

    def __ge__(self, other):
        return len(self.lst_words) >= len(other)


d = {StringText(i): i for i in lst}
lst_text = list(d.keys())
lst_text_sorted = sorted(lst_text, reverse=True)
lst_final = [d[obj] for obj in lst_text_sorted]
a = [' '.join(stroka) for stroka in lst_final]
print(lst_text, lst_text_sorted, lst_final, a, sep='\n')

