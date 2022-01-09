class PokerGame():

    def __init__(self, current_players, deck):

        deck.shuffle()
        self.community_cards = []
        self.current_players = current_players
        self.deck = deck

        while True:
            ans = input("Ready for the cards to be dealt? y/n ")

            if ans == "y":
                deck.shuffle()

                for player in current_players:
                    player.hand.clear()

                print("\nDealing pocket cards...\n")
                self.deal_cards()
                print(f"Length of deck is...{len(deck.deck)}")
            elif ans == "n":
                deck.hard_shuffle()
                break

    def deal_cards(self):

        for n in range(2):
            for player in self.current_players:
                card = self.deck.deck.pop()
                player.hand.append(card)

        for player in self.current_players:
            print(f"{player.username}'s cards are, {player.hand}")
