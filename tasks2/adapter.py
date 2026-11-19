from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount_uzs: int) -> str: ...


class PaymeProcessor(PaymentProcessor):
    def pay(self, amount_uzs):
        return f"Payme orqali {amount_uzs:,} so'm to'landi"


class ForeignStripeAPI:
    def make_charge(self, cents: int, currency: str) -> dict:
        return {"status": "ok", "charged": cents, "currency": currency}


class StripeAdapter(PaymentProcessor):
    USD_RATE = 12_800

    def __init__(self, stripe: ForeignStripeAPI):
        self._stripe = stripe

    def pay(self, amount_uzs):
        cents = round(amount_uzs / self.USD_RATE * 100)
        res = self._stripe.make_charge(cents, "USD")
        return f"Stripe orqali {res['charged'] / 100:.2f} USD to'landi ({amount_uzs:,} so'm)"


def checkout(processor: PaymentProcessor, amount):
    print(" ", processor.pay(amount))


if __name__ == "__main__":
    print("=== Adapter ===")
    checkout(PaymeProcessor(), 256_000)
    checkout(StripeAdapter(ForeignStripeAPI()), 256_000)
