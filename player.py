class Player():
    """ A class to represent a plyer in a poker game"""

    def __init__(self, username, ID, funds=0):
        self.username = username
        self.hand = None
        self.funds = 0
        self.ID = ID

        print(
            f"{self.username} has entered the game.\n"
        )

    def __str__(self):
        return(
            f"{self.username}\n"
            f"Funds: ${self.funds}\n"
            f"ID: {self.ID}\n"
        )

    def deposit(self, amount):
        self.funds = amount + self.funds
