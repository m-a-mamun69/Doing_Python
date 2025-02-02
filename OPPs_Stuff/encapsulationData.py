# Understanding Encapsulation For Protect Your Data
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private Attribute
    #For Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    #Getting Balance
    def get_balance(self):
        return self.__balance

account = BankAccount(2000)
account.deposit(450)
print("Total: ",account.get_balance())