from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str: ...


class Truck(Transport):
    def deliver(self):
        return "Yuk mashinasida yo'l orqali yetkazildi"


class Ship(Transport):
    def deliver(self):
        return "Kemada dengiz orqali yetkazildi"


class Plane(Transport):
    def deliver(self):
        return "Samolyotda havo orqali yetkazildi"


class TransportFactory:
    _registry = {"truck": Truck, "ship": Ship, "plane": Plane}

    @classmethod
    def create(cls, kind: str) -> Transport:
        try:
            return cls._registry[kind]()
        except KeyError:
            raise ValueError(f"Noma'lum transport turi: {kind}")


class Notification(ABC):
    @abstractmethod
    def send(self, msg: str) -> str: ...


class EmailNotification(Notification):
    def send(self, msg):
        return f"Email yuborildi: {msg}"


class SmsNotification(Notification):
    def send(self, msg):
        return f"SMS yuborildi: {msg}"


class Notifier(ABC):
    @abstractmethod
    def create_notification(self) -> Notification: ...

    def notify(self, msg):
        return self.create_notification().send(msg)


class EmailNotifier(Notifier):
    def create_notification(self):
        return EmailNotification()


class SmsNotifier(Notifier):
    def create_notification(self):
        return SmsNotification()


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


class LightButton(Button):
    def render(self):
        return "[ Oq tugma ]"


class DarkButton(Button):
    def render(self):
        return "[ Qora tugma ]"


class LightCheckbox(Checkbox):
    def render(self):
        return "[x] Oq checkbox"


class DarkCheckbox(Checkbox):
    def render(self):
        return "[x] Qora checkbox"


class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()


class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()


def render_ui(factory: UIFactory):
    print(" ", factory.create_button().render(), "|", factory.create_checkbox().render())


if __name__ == "__main__":
    print("=== Task 1: Simple Factory ===")
    for kind in ("truck", "ship", "plane"):
        print(f"  {kind}: {TransportFactory.create(kind).deliver()}")

    print("\n=== Task 2: Factory Method ===")
    for notifier in (EmailNotifier(), SmsNotifier()):
        print(" ", notifier.notify("Buyurtmangiz tayyor"))

    print("\n=== Bonus: Abstract Factory ===")
    render_ui(LightThemeFactory())
    render_ui(DarkThemeFactory())
