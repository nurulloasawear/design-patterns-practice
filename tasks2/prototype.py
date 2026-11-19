import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x=0, y=0, color="qora", tags=None):
        self.x, self.y, self.color = x, y, color
        self.tags = tags if tags is not None else []

    def clone(self):
        return copy.deepcopy(self)

    @abstractmethod
    def area(self) -> float: ...


class Circle(Shape):
    def __init__(self, radius=1, **kw):
        super().__init__(**kw)
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

    def __str__(self):
        return f"Circle(r={self.radius}, ({self.x},{self.y}), {self.color}, tags={self.tags})"


class Rectangle(Shape):
    def __init__(self, w=1, h=1, **kw):
        super().__init__(**kw)
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return f"Rectangle({self.w}x{self.h}, ({self.x},{self.y}), {self.color}, tags={self.tags})"


class Document:
    def __init__(self, title, body, meta):
        self.title, self.body, self.meta = title, body, meta

    def clone(self, **changes):
        doc = copy.deepcopy(self)
        for k, v in changes.items():
            setattr(doc, k, v)
        return doc

    def __str__(self):
        return f"<{self.title}> {self.body!r} meta={self.meta}"


class PrototypeRegistry:
    def __init__(self):
        self._items = {}

    def register(self, name, proto):
        self._items[name] = proto

    def create(self, name, **changes):
        return self._items[name].clone(**changes)


if __name__ == "__main__":
    print("=== Task 1: Shape.clone() ===")
    c1 = Circle(radius=5, x=10, y=20, color="qizil", tags=["asosiy"])
    c2 = c1.clone()
    c2.color = "ko'k"
    c2.tags.append("nusxa")
    print("  Asl:  ", c1, "yuza:", c1.area())
    print("  Klon: ", c2)
    print("  Ichki ro'yxat alohida:", c1.tags is not c2.tags)

    shallow = copy.copy(c1)
    shallow.tags.append("sayoz")
    print("  Sayoz nusxada asl ham o'zgaradi:", c1.tags)

    print("\n=== Task 2: PrototypeRegistry ===")
    reg = PrototypeRegistry()
    reg.register("invoice", Document("Hisob-faktura", "Summa: ___", {"type": "moliya"}))
    reg.register("letter", Document("Xat", "Hurmatli ___,", {"type": "rasmiy"}))
    d1 = reg.create("invoice", body="Summa: 1 000 000 so'm")
    d2 = reg.create("letter", body="Hurmatli Ali,")
    d1.meta["paid"] = True
    print(" ", d1)
    print(" ", d2)
    print("  Shablon o'zgarmadi:", reg.create("invoice"))
