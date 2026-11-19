from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int: ...

    @abstractmethod
    def description(self) -> str: ...


class Espresso(Coffee):
    def cost(self):
        return 15_000

    def description(self):
        return "Espresso"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


class Milk(CoffeeDecorator):
    def cost(self):
        return super().cost() + 4_000

    def description(self):
        return super().description() + " + sut"


class Syrup(CoffeeDecorator):
    def cost(self):
        return super().cost() + 5_000

    def description(self):
        return super().description() + " + sirop"


class ExtraShot(CoffeeDecorator):
    def cost(self):
        return super().cost() + 7_000

    def description(self):
        return super().description() + " + qo'shimcha shot"


if __name__ == "__main__":
    print("=== Decorator ===")
    orders = [
        Espresso(),
        Milk(Espresso()),
        Syrup(Milk(ExtraShot(Espresso()))),
    ]
    for c in orders:
        print(f"  {c.description():45} {c.cost():>7,} so'm")
