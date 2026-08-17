class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
    def deposit(self,amount,description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,description = ""):
        self.ledger.append({"amount": -amount, "description": description})
        return True

def create_spend_chart(categories):
    pass