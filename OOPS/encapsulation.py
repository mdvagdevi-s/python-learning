class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
    def show_balance(self):
        print("Balance is:",self._balance)
acc=BankAccount(1000)
acc.deposit(10000)
acc.show_balance()