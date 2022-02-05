from ledger import Ledger


class Player():
    """ A class to represent a plyer in a poker game"""

    def __init__(self, username, ID):
        self.username = username
        self.hand = []
        self.ID = ID
        self.ledger = Ledger(self.ID)
        self.ledger.deposit(1000, description="Initial Deposit")
        print(self.ledger)

        self.choices = {
            "Fold": 'off',
            "Check": 'off',
            "Call": 'off',
            "Raise": 'off',
            "Bet": 'off',
        }

        self.ready = False
        self.active = False
        self.blind = False
        self.turn = False
        self.went = False
        self.fold = False

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
