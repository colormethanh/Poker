class Player():
    """ A class to represent a plyer in a poker game"""

    def __init__(self, username, ID):
        self.username = username
        self.hand = []
        self.ledger = []
        #self.funds = 0
        self.ID = ID

        print(
            f"{self.username} has entered the game.\n"
        )

    def __str__(self):
        return(
            f"Username: {self.username}\n"
            f"Funds: ${self.get_balance()}\n"
            f"ID: {self.ID}\n"
        )

    def get_balance(self):
        balance = sum([i.get("amount") for i in self.ledger])
        return(balance)

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        elif self.get_balance() < amount:
            return False

    def deposit(self, amount, description):
        dep = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(dep)

    def widthdraw(self, amount, description):
        if self.check_funds(amount):
            act_widthdraw = {
                "amount": int(f"-{amount}"),
                "description": description
            }
            self.ledger.append(act_widthdraw)
            return True
        else:
            return False
