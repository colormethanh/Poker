from game_stats import GameStats
import game_functions as GF
from cards import Cards
from main_game import PokerGame


def run():
    GS = GameStats()
    deck = Cards()
    poker_game = PokerGame(GS, deck)
    GF.add_player(GS, p_name="thanh", ID="111", Funds=False)
    GF.home_screen(GS, deck, poker_game)


run()
