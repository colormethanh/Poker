import game_stats as GS

class Game():
    
    def __init__(self):
        txt = ["Welcome to my Poker games!",
                "To continue please select...",
                "1. Start",
                "2. Quit",
                ""
                ]
        
        
        while True:
            for l in txt: print(l)
            sel = input("Type response here! ")
        
            if int(sel) not in range(1,3):
                print ("oops, please responde with 1 or 2\n")
                continue
            elif sel == "1":
                print ("Starting game...")
                self.game_options()
                break
            elif sel == "2":
                break
                
    def game_options(self):
        txt = [
            "Game options are..",
            "1. Start New Hand",
            "2. Add Player",
            "3. See Current Players",
            "4. Quit Game",
            ""
            ]
        
        while True:
            for l in txt: print(l)
            sel = input("Make your selection here! ")
            
            if int(sel) not in range(1,5):
                print ("Oops, valid responses are numbers 1 to 4\n")
                continue
            elif sel == "1":
                print ("Starting new hand...")
                break
            elif sel == "2":
                print("Adding player...")
                break
            elif sel == "3":
                print("Current players are...")
                for i in GS.current_players: print(i)
                break
            elif sel == "4":
                break
        
        
        
        
        
        
            
poker = Game()