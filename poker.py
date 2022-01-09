from game_stats import GameStats
import game_functions as GF
from cards import Cards


def run():
    GS = GameStats()
    deck = Cards()
    GF.home_screen(GS, deck)


run()
