class bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= money

    def show(self):
        print(self.balance)

account = {}

while True:
    line = input().split()
    action = line[0]

    if action == "stop":
        break

    name = line[1]

    if action == "create":
        money = int(line[2])
        account[name] = bank(name, money)

    elif action == "deposit":
        money = int(line[2])
        if name not in account:
            print("Account not found")
        else:
            account[name].deposit(money)

    elif action == "withdraw":
        money = int(line[2])
        if name not in account:
            print("Account not found")
        else:
            account[name].withdraw(money)

    elif action == "balance":
        if name not in account:
            print("Account not found")
        else:
            account[name].show()