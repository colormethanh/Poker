import random


class Cards():

    def __init__(self):
        self.suits = ["hearts", "diamonds", "clovers", "spades"]
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.deck = [(num, suit) for suit in self.suits for num in self.nums]

    def __str__(self):
        msg = []
        for c in self.deck:
            msg.append(str(c))

        msg = ",".join(msg)
        return(msg)

    def shuffle(self):
        random.shuffle(self.deck)
        return(self.deck)

    def hard_shuffle(self):
        self.deck = [(num, suit) for suit in self.suits for num in self.nums]
        random.shuffle(self.deck)
        return(self.deck)


cards = Cards()

card = cards.deck[1]

print(card)

print(card[0])
print(card[1])
