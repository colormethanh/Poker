from game_stats import GameStats
import game_functions as GF
from cards import Cards
from main_game import PokerGame


def run():
    # initializing Game Stats, deck, and poker game
    GS = GameStats()
    deck = Cards()
    poker_game = PokerGame(GS, deck)

    # starting the game's home home_screen
    GF.home_screen(GS, deck, poker_game)


run()
