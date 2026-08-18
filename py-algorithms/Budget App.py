class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
    def deposit(self,amount,description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            # Extract the amount from the dictionary and add it to the running total
            total += item["amount"]
        # Return the final total AFTER the loop has finished iterating
        return total

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer(self,amount,category):
        if self.check_funds(amount): 
            # Call your own withdraw method
            self.withdraw(amount,f"Transfer to {self.name}") #BUGGED
            # Call the other category's deposit method
            category.deposit(amount,f"Transfer from {self.name}") #BUGGED
            return True
        else:
            return False

    def __str__(self):
        title = self.name.center(30, "*")
        output = title + "\n"
        
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            output += f"{desc:<23}{amt:>7}/n"

        output += F"Total:{self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    pass