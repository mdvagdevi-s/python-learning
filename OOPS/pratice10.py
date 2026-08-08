class bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount

    def show_balance(self):
        return self.__balance

acc=bank(1000)
acc.deposit(200)
acc.withdraw(500)
print(acc.show_balance())
