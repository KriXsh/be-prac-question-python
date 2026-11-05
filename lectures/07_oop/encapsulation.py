"""
Encapsulation
Keep data and the methods that use it together in a class,
and hide the data so it can only be changed through those methods.
In Python, a name starting with __ is "private" (not accessible from outside).
"""


class BankAccount():
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        # rule enforced inside the class
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(2000)  # Insufficient balance
print(account.get_balance())  # 1500

# print(account.__balance)  # AttributeError: no direct access to private data
