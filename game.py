from player import Player
import random


class Game:
    def __init__(self):
        self.deck = self.get_deck()
        self.deck = self.shuffle_deck()
        self.action_log = []
        self.community_cards = []
        self.players = [
            Player("Carl", 1),
            Player("Dan", 2),
            Player("Lois", 3),
            Player("Charles", 4),
            Player("Bessie", 5)
        ]

    def get_deck(self):
        suits = ["hearts", "diamonds", "clovers", "spades"]
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        deck = [(num, suit) for suit in suits for num in nums]
        return deck

    def check_deck(self, cards_needed):

        if len(self.deck) < cards_needed:
            return False
        else:
            return True

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return(self.deck)

    def deal(self, user_num):

        for n in range(2):
            card = self.deck.pop()
            self.players[user_num - 1].hand.append(card)
            self.action_log.insert(0, f"player {user_num}, was dealt {card}")

    def record_action(self, action, player_num):
        self.action_log.insert(0, f"Player {player_num} has {action}")
        return self.action_log

    def hard_shuffle(self):
        self.deck = self.get_deck()
        random.shuffle(self.deck)
        return(self.deck)

    def reset(self):

        for p in self.players:
            p.hand.clear()

        self.community_cards.clear()
        self.deck = self.hard_shuffle()
        self.action_log.clear()
