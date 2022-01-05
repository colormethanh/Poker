class Player():
    """ A class to represent a plyer in a poker game"""
    def __init__(self, username, funds = 0):
        self.username = username 
        self.hand = None
        
        print(f"Player {self.username} has entered the game.\nThey have a total of ${funds} to spend.")

player_1 = Player("player_1")