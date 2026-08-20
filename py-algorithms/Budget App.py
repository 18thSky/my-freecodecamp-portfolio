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
            self.withdraw(amount, f"Transfer to {category.name}")
            # Call the other category's deposit method
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        title = self.name.center(30, "*")
        output = title + "\n"
        
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            output += f"{desc:<23}{amt:>7}\n"

        output += F"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        tracker = 0
        for transaction in category.ledger:
            if transaction["amount"] <= 0:
                tracker += abs(transaction["amount"])
        spent_amounts.append(tracker)

    total_spent = sum(spent_amounts)
    percentages = []
    for amount in spent_amounts:
        percent = amount/total_spent * 100
        rounded_number = int(percent/10) *10
        percentages.append(rounded_number)

    chart = "Percentage spent by category\n"
    for i in range(100,-1,-10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart +="   "
        chart += "\n"

    chart += "    " + "-" * ((len(categories) * 3) + 1) + "\n"

    max_length = 0 
    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)
        
    for i in range(max_length):
        # FIX 1: Type exactly FIVE standard spaces here
        chart += "     "
        
        for category in categories:
            if i < len(category.name):
                # Type exactly TWO standard spaces after the letter
                chart += category.name[i] + "  "
            else:
                # Type exactly THREE standard spaces here
                chart += "   "
                
        if i < max_length - 1:
            chart += "\n"

    return chart

