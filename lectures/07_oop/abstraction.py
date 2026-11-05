"""
Abstraction
Hide the "how" and show only the "what".
An abstract class defines methods that every subclass MUST implement.
You cannot create an object of an abstract class directly.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    # every payment type must implement pay()
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# user only calls pay(), doesn't care how each one works inside
payment = CardPayment()
payment.pay(500)
payment = UpiPayment()
payment.pay(200)

# payment = Payment()  # TypeError: Can't instantiate abstract class Payment
