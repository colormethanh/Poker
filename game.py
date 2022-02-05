from player import Player
from ledger import Ledger
import random


class Game:
    def __init__(self):
        self.deck = self.get_deck()
        self.deck = self.shuffle_deck()
        self.ledger = Ledger("Pot")
        print(self.ledger)

        self.action_log = []
        self.community_cards = []
        self.active_plyrs = []
        self.prev_bet = 0

        # game settings
        self.big_blind = 10
        self.small_blind = 5
        self.ante = 5

        # game state info
        self.active = False
        self.blind_assnd = False
        self.ante_collected = False
        self.pocket_dealt = False
        self.plyer_turn = 0
        self.plyr_bet = False
        self.pocket_dealt = False

        self.players_mstr = [
            Player("Carl", 1),
            Player("Dan", 2),
            Player("Lois", 3),
            Player("Charles", 4),
            Player("Bessie", 5)
        ]

    def get_active_plyrs(self):
        self.active_plyrs = []

        for player in self.players_mstr:
            if player.active:
                self.active_plyrs.append(player)

        return self.active_plyrs

    def chk_ready(self):
        ct = 0
        for player in self.get_active_plyrs():
            if not player.ready:
                return False
            else:
                ct += 1
                continue

        if ct >= 2:
            return True
        else:
            return False

    def chk_phase(self):

        if self.chk_ready():
            if self.pocket_dealt:
                game_phase = "pre-flop"
                return game_phase
            else:
                game_phase = "pre-pocket"
                return game_phase
        else:
            game_phase = "waiting"
            return game_phase

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

    def deal_cards(self):
        """ Deals all active users their cards """
        for c in range(2):
            for p in self.get_active_plyrs():
                card = self.deck.pop()
                p.hand.append(card)
                self.action_log.insert(0, f"Player {p.ID} was dealt their hand")

    def hard_shuffle(self):
        self.deck = self.get_deck()
        random.shuffle(self.deck)
        return(self.deck)

    def reset(self):

        for p in self.players_mstr:
            p.hand.clear()
            p.ready = False
            p.active = False

        self.community_cards.clear()
        self.deck = self.hard_shuffle()
        self.action_log.clear()

    def assign_blinds(self, game_start=False):

        if game_start:
            p = self.get_active_plyrs()
            p[0].blind = "Small Blind"
            self.action_log.insert(0, f"Player {p[0].ID} is the Small Blind")

            p[1].blind = "Big Blind"
            self.action_log.insert(0, f"Player {p[1].ID} is the Big Blind")
        else:
            for p in self.get_active_plyrs():
                if p.blind == "Small Blind":
                    p.blind = False

                if p.blind == "Big Blind":
                    p.blind = "Small Blind"
                    self.action_log.insert(0, f"Player {p.ID} is the Small Blind")
                    break

            try:
                for p in self.get_active_plyrs():
                    if p.blind == "Small Blind":
                        self.active_plyrs[p.ID].blind = "Big Blind"
                        self.action_log.insert(0, f" player {p.ID} is the Big Blind")
                        break
            except:
                p = self.get_active_plyrs()
                p[0].blind = "Big Blind"
                self.action_log.insert(0, f"Player {p[0].ID} is the Big Blind")

        self.blind_assnd = True

    def pre_pocket_bet(self, player_obj):

        if not player_obj.turn:
            for k, v in player_obj.choices.items():
                player_obj.choices[k] = "off"
        else:
            for k, v in player_obj.choices.items():
                player_obj.choices[k] = "on"
