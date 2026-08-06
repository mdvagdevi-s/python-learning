class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def show_balance(self):
        print("Balance is:",self.balance)
acc=BankAccount(1000)
acc.deposit(10000)
acc.show_balance()