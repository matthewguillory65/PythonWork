import random

class Player(object):
    def __init__(self, name):
        self._name = name
        self._card = []

    def add_cards(self, cards):
        self._card.append(cards)
        return cards



Thecards = [['Light', 5], ['Dark', 10]]

a = Player('    Matthew')
a._name
a.add_cards(random.choice(Thecards))
a.add_cards(random.choice(Thecards))
a.add_cards(random.choice(Thecards))
a.add_cards(random.choice(Thecards))
a.add_cards(random.choice(Thecards))

b = Player('    Zyron')
b._name
b.add_cards(random.choice(Thecards))
b.add_cards(random.choice(Thecards))
b.add_cards(random.choice(Thecards))
b.add_cards(random.choice(Thecards))
b.add_cards(random.choice(Thecards))

def HigherPoints(player1, player2):
    guy = 0
    guy2 = 0

    for x in range(4):
        guy = guy + player1._card[x][1]
    for y in range(4):
        guy2 = guy2 + player2._card[y][1]
    
    return [player1._name, guy] if guy > guy2 else [player2._name, guy2]

print HigherPoints(a, b)