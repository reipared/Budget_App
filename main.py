class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

def create_spend_chart(categories):
    # calculate total withdrawals for each category
    withdrawals = []
    for category in categories:
        total_withdrawals = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_withdrawals += abs(item['amount'])
        withdrawals.append(total_withdrawals)

    # calculate percentage spent for each category
    percentages = []
    total_withdrawals = sum(withdrawals)
    for withdrawal in withdrawals:
        percentage = int(withdrawal / total_withdrawals * 100)
        percentages.append(percentage)

    # create chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # determine longest category name
    max_name_length = max([len(category.name) for category in categories])

    # add category names to chart
    for i in range(max_name_length):
        chart += " " * 5
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())  # should print 973.96
print(food)  # should print a formatted ledger

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(clothing.get_balance())  # should
