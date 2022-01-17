from player import Player
import random


class Game:
    def __init__(self):
        self.deck = self.get_deck()
        self.deck = self.shuffle_deck()
        self.action_log = []
        self.players = [
            Player("Carl", 1),
            Player("Dan", 2),
            Player("Lois", 3),
            Player("Charles", 4),
            Player("Bessie", 5)
        ]

    def get_deck(self):
        suits = ["hearts", "diamonds", "clover", "spades"]
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        deck = [(num, suit) for suit in suits for num in nums]
        return deck

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return(self.deck)

    def deal(self, user_num):
        for n in range(2):
            card = self.deck.pop()
            self.players[user_num - 1].hand.append(card)

    def record_action(self, action, player_num):
        self.action_log.insert(0, f"Player {player_num} has {action}")
        return self.action_log
