class Inventory:
    def check(self, product, qty):
        print(f"  [Ombor] {product} x{qty} mavjud")
        return True

    def reserve(self, product, qty):
        print(f"  [Ombor] {product} x{qty} band qilindi")


class Payment:
    def charge(self, user, amount):
        print(f"  [To'lov] {user} dan {amount:,} so'm yechildi")
        return True


class Shipping:
    def ship(self, user, product):
        print(f"  [Yetkazish] {product} -> {user} manziliga jo'natildi")
        return "TRK-12345"


class NotificationService:
    def send(self, user, msg):
        print(f"  [Xabar] {user}: {msg}")


class OrderFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()
        self.notifier = NotificationService()

    def place_order(self, user, product, qty, price):
        if not self.inventory.check(product, qty):
            return None
        self.inventory.reserve(product, qty)
        if not self.payment.charge(user, qty * price):
            return None
        track = self.shipping.ship(user, product)
        self.notifier.send(user, f"Buyurtma qabul qilindi, trek raqam: {track}")
        return track


if __name__ == "__main__":
    print("=== Facade ===")
    track = OrderFacade().place_order("Ali", "Noutbuk", 1, 9_500_000)
    print("Natija:", track)
