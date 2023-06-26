class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score != 0


lst_in = ['Balakirev; 34; 2048', 'Mediel; 27; 0', 'Vlad; 18; 9012', 'Nina P; 33; 0']

lst = [string.split('; ') for string in lst_in]
lst = [[el[0], int(el[1]), int(el[2])] for el in lst]
players = []
for el in lst:
    players.append(Player(*el))

players_filtered = list(filter(lambda x: bool(x), players))
print(players_filtered)
