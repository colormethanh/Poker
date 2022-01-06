from player import Player


def home_screen(GS):
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
            print("Starting game...")
            game_options(GS)
            break
        elif sel == "2":
            break


def game_options(GS):
    txt = [
        "\nGame options are..",
        "1. Start New Hand",
        "2. Add Player",
        "3. See Current Players",
        "4. Quit Game",
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
            print("Starting new hand...\n")
            continue

        elif sel == "2":
            add_player(GS)

        elif sel == "3":
            print("Current players...\n")
            if len(GS.current_players) == 0:
                print("There are currently no players in the game\n")
            else:
                for p in GS.current_players:
                    print(p)
            continue
        elif sel == "4":
            print("See you next time!")
            break


def add_player(GS):  # need to add checks for user ID
    p_name = input("Username: ")
    ID = input("Please choose 3 numbers as your ID: ")
    player = Player(p_name, ID)

    while True:
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
