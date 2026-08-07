class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount

    def show_balance(self):
        return self.balance

acc=bank(1000)
acc.deposit(2000)
acc.withdraw(500)
print(acc.show_balance())
