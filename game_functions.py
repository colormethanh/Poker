import sys
from player import Player


def home_screen(GS, deck, poker_game):
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
            print("oops, please respond with 1 or 2\n")
            continue
        elif sel == "1":
            print("Starting game...\n")
            game_options(GS, deck, poker_game)
            break
        elif sel == "2":
            print("See you next time!")
            sys.exit()


def game_options(GS, deck, poker_game):
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
            new_hand(GS, deck, poker_game)

        elif sel == "2":
            add_player(GS)

        elif sel == "3":
            view_players(GS)

        elif sel == "4":
            home_screen(GS, deck, poker_game)


def add_player(GS, p_name=None, ID=None, Funds=True):

    if not p_name:
        p_name = input("Username: ")
    if not ID:
        ID = input("Please choose 3 numbers as your ID: ")

    player = Player(p_name, ID)

    if Funds:
        enter_funds = cont_box(q="Enter Funds? y/n ")

        if enter_funds:
            amount = input("How much? ")
            player.deposit(int(amount), "Initial Deposit")

    GS.current_players.append(player)

    add_another = cont_box(q="Add another player? y/n ")
    if add_another:
        add_player(GS)


def view_players(GS):
    print("Current players...\n")

    if len(GS.current_players) == 0:
        print("There are currently no players in the game\n")
    else:
        for p in GS.current_players:
            print(p)


def new_hand(GS, deck, poker_game):

    if len(GS.current_players) >= 1:
        poker_game.start_game()
    else:
        print("Oops please add at least one player to start a game!\n")

        cont = cont_box(q="Would you like to add now? ^_^ y/n ")
        if cont:
            add_player(GS)

        print("\nReturning to game options...")
        game_options(GS, deck, poker_game)


def cont_box(q="Continue? y/n"):

    while True:
        ans = input(q)
        if ans == "y":
            return(True)
        elif ans == "n":
            return(False)
        else:
            print("Opps, valid answers are 'y' and 'n', please try again")
            continue
