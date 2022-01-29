from player import Player
import random


class Game:
    def __init__(self):
        self.deck = self.get_deck()
        self.deck = self.shuffle_deck()
        self.action_log = []
        self.community_cards = []
        self.active_plyrs = []
        self.prev_bet = 0
        self.big_blind = 4
        self.small_blind = 2
        self.ante = 1
        self.plyer_turn = 0

        self.plyr_bet = False

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
        for player in self.active_plyrs:
            if not player.ready:
                return False
            else:
                continue
        return True

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
            for p in self.active_plyrs:
                card = self.deck.pop()
                p.hand.append(card)
                self.action_log.insert(0, f"Player {p.ID}, was dealt a card.")

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
            self.action_log.insert(0, f"Player {p[0].ID} has been assigned Small Blind")

            p[1].blind = "Big Blind"
            self.action_log.insert(0, f"Player {p[1].ID} has been assigned Big Blind")
        else:
            for p in self.get_active_plyrs():
                if p.blind == "Small Blind":
                    p.blind = False

                if p.blind == "Big Blind":
                    p.blind = "Small Blind"
                    self.action_log.insert(0, f"Player {p.ID} been assigned Small Blind")
                    break

            try:
                for p in self.get_active_plyrs():
                    if p.blind == "Small Blind":
                        self.active_plyrs[p.ID].blind = "Big Blind"
                        self.action_log.insert(0, "been assigned Big Blind")
                        break
            except:
                p = self.get_active_plyrs()
                p[0].blind = "Big Blind"
                self.action_log.insert(0, f"Player {p[0].ID} has been assigned Big Blind")

    def pre_pocket_bet(self, p_num):
        player = self.players_mstr[p_num - 1]

        for p in self.get_active_plyrs():

            if not p.turn:
                player.choices["fold"] = False
                player.choices["check"] = False
                player.choices["call"] = False
                player.choices["raise"] = False
                player.choices["bet"] = False
            if p.turn:
                if self.plyr_bet:
                    player.choices["fold"] = True
                    player.choices["call"] = True
                    player.choices["raise"] = True


game = Game()

for p in game.players_mstr:
    print(f"Player {p.ID} Is... {p.blind}")

for p in range(2):
    game.players_mstr[p].active = True
    game.players_mstr[p].ready = True

game.assign_blinds(game_start=True)

print("_____" * 20)

for p in game.players_mstr:
    print(f"Player {p.ID} Is... {p.blind}")

game.assign_blinds(game_start=False)

print("_____" * 20)

for p in game.players_mstr:
    print(f"Player {p.ID} Is... {p.blind}")

for action in game.action_log:
    print(action)
