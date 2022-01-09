import sys
from player import Player
from main_game import PokerGame


def home_screen(GS, deck):
    txt = ["Welcome to my Poker games!",
           "To continue please select...",
           "1. Start",
           "2. Quit",
           ""
           ]

    while True:
        for ln in txt:
            print(ln)
        sel = input("Type response here! ")

        if int(sel) not in range(1, 3):
            print("oops, please responde with 1 or 2\n")
            continue
        elif sel == "1":
            add_player(GS, p_name="thanh", ID="111", Funds=False)

            print("Starting game...\n")
            game_options(GS, deck)
            break
        elif sel == "2":
            print("See you next time!")
            sys.exit()


def game_options(GS, deck):
    txt = [
        "\nGame options are..",
        "1. Start New Hand",
        "2. Add Player",
        "3. See Current Players",
        "4. back to title screen",
        ""
    ]

    while True:
        for ln in txt:
            print(ln)
        sel = input("Make your selection here! ")

        if sel == "" or int(sel) not in range(1, 5):
            print("Oops, valid responses are numbers 1 to 4\n")
            continue

        elif sel == "1":
            new_hand(GS, deck)

        elif sel == "2":
            add_player(GS)

        elif sel == "3":
            view_players(GS)

        elif sel == "4":
            home_screen(GS, deck)


def add_player(GS, p_name=None, ID=None, Funds=True):

    if not p_name:
        p_name = input("Username: ")
    if not ID:
        ID = input("Please choose 3 numbers as your ID: ")

    player = Player(p_name, ID)

    while Funds:
        p_funds = input("Enter funds? y or n: ")

        if p_funds == "y":
            amount = input("How much? ")
            player.deposit(int(amount))
            break
        elif p_funds == "n":
            break
        else:
            print("Oops, valid responses are y and n.")
            continue

    GS.current_players.append(player)


def view_players(GS):
    print("Current players...\n")
    if len(GS.current_players) == 0:
        print("There are currently no players in the game\n")
    else:
        for p in GS.current_players:
            print(p)


def new_hand(GS, deck):

    if len(GS.current_players) >= 1:
        PokerGame(GS.current_players, deck)
    else:
        print("Oops please add at least one player to start a game!")

        while True:
            ans = input("Would you like to add one now? ^_^ y/n ")
            if ans == "y":
                add_player(GS)
                break
            elif ans == "n":
                print("Returning to game options...")
                game_options(GS, deck)
            else:
                print("Opps, valid answers are 'y' and 'n', please try again")
