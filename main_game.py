import game_functions as GF


class PokerGame():

    def __init__(self, GS, deck):

        self.GS = GS
        self.current_players = GS.current_players
        self.deck = deck

        deck.shuffle()
        self.community_cards = []

    def start_game(self):

        # start game prompt
        start = GF.cont_box(q="Ready to deal hands? y/n ")

        while start:

            # reseting player hands, deck, and community_cards
            self.deck.hard_shuffle()
            self.community_cards.clear()
            for p in self.current_players:
                p.hand.clear()

            self.deal_pocket()
            print(f"Legnth of cards are {len(self.deck.deck)}")

            self.the_flop()
            print(f"Legnth of cards are {len(self.deck.deck)}")

            self.deal_card(question="Ready for the turn? y/n ")
            print(f"Legnth of cards are {len(self.deck.deck)}")

            self.deal_card(question="Ready for the River? y/n ")
            print(f"Legnth of cards are {len(self.deck.deck)}")
            # end of one game ###

            # prompt to reset game
            start = GF.cont_box(q="Ready for another hand? y/n ")
            if start:
                continue
            if not start:
                break
        GF.game_options(self.GS, self.deck, self)

    def deal_pocket(self):
        print("\nDealing 'pocket cards'...\n")

        for n in range(2):
            for player in self.current_players:
                card = self.deck.deck.pop()
                player.hand.append(card)

        for player in self.current_players:
            print(f"{player.username}'s cards are, {player.hand}\n")

    def the_flop(self):
        flop = GF.cont_box(q="Ready for the flop? y/n ")

        if flop:
            for i in range(3):
                card = self.deck.deck.pop()
                self.community_cards.append(card)
            print(f"\nCommunity cards are... {self.community_cards}")
        else:
            GF.game_options(self.GS, self.deck, self)

    def deal_card(self, question):

        deal = GF.cont_box(q=question)

        if deal:
            card = self.deck.deck.pop()
            self.community_cards.append(card)
            print(f"\nCommunity cards are... {self.community_cards}")
        else:
            GF.game_options(self.GS, self.deck, self)
