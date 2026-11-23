# Инкапсуляция
print()
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money!")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(100)

account.deposit(50)
account.withdraw(30)
account.show_balance()