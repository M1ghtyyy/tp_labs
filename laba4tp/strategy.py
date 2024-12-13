from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, name: str, card_number: str):
        self.name = name
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card (Card Number: {self.card_number}).")

class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number: str):
        self.account_number = account_number

    def pay(self, amount: float):
        print(f"Paid {amount} using Bank Transfer (Account Number: {self.account_number}).")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount: float):
        self._strategy.pay(amount)

# Example usage
if __name__ == "__main__":
    credit_card = CreditCardPayment(name="Vovan Belyaev", card_number="1234-5678-9876-5432")
    bank_transfer = BankTransferPayment(account_number="987654321")

    context = PaymentContext(strategy=credit_card)
    context.execute_payment(100.0)

    context.set_strategy(strategy=bank_transfer)
    context.execute_payment(300.0)
