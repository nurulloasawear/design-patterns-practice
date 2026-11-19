from dataclasses import dataclass, field


@dataclass
class Computer:
    cpu: str = ""
    ram_gb: int = 0
    storage: str = ""
    gpu: str | None = None

    def __str__(self):
        gpu = self.gpu or "integratsiyalangan"
        return f"CPU={self.cpu}, RAM={self.ram_gb}GB, Disk={self.storage}, GPU={gpu}"


class ComputerBuilder:
    def __init__(self):
        self._pc = Computer()

    def cpu(self, cpu):
        self._pc.cpu = cpu
        return self

    def ram(self, gb):
        self._pc.ram_gb = gb
        return self

    def storage(self, s):
        self._pc.storage = s
        return self

    def gpu(self, g):
        self._pc.gpu = g
        return self

    def build(self) -> Computer:
        if not self._pc.cpu or not self._pc.ram_gb:
            raise ValueError("CPU va RAM majburiy")
        pc, self._pc = self._pc, Computer()
        return pc


class QueryBuilder:
    def __init__(self, table):
        self._table = table
        self._fields = ["*"]
        self._where = []
        self._order = None
        self._limit = None

    def select(self, *fields):
        self._fields = list(fields)
        return self

    def where(self, condition):
        self._where.append(condition)
        return self

    def order_by(self, field, desc=False):
        self._order = f"{field} {'DESC' if desc else 'ASC'}"
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self) -> str:
        sql = f"SELECT {', '.join(self._fields)} FROM {self._table}"
        if self._where:
            sql += " WHERE " + " AND ".join(self._where)
        if self._order:
            sql += f" ORDER BY {self._order}"
        if self._limit is not None:
            sql += f" LIMIT {self._limit}"
        return sql + ";"


@dataclass
class Pizza:
    size: str = "o'rta"
    dough: str = "oddiy"
    toppings: list = field(default_factory=list)

    def __str__(self):
        return f"{self.size} pizza, xamir: {self.dough}, ustida: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza()

    def set_size(self, size):
        self._pizza.size = size

    def set_dough(self, dough):
        self._pizza.dough = dough

    def add_topping(self, t):
        self._pizza.toppings.append(t)

    def get_result(self):
        p = self._pizza
        self.reset()
        return p


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_margherita(self):
        b = self.builder
        b.set_size("o'rta")
        b.set_dough("yupqa")
        b.add_topping("pomidor sousi")
        b.add_topping("motsarella")
        return b.get_result()

    def make_pepperoni(self):
        b = self.builder
        b.set_size("katta")
        b.set_dough("qalin")
        for t in ("pomidor sousi", "motsarella", "pepperoni"):
            b.add_topping(t)
        return b.get_result()


if __name__ == "__main__":
    print("=== Task 1: ComputerBuilder ===")
    gaming = ComputerBuilder().cpu("Ryzen 9").ram(32).storage("2TB NVMe").gpu("RTX 4080").build()
    office = ComputerBuilder().cpu("Core i3").ram(8).storage("256GB SSD").build()
    print("  O'yin PC:", gaming)
    print("  Ofis PC: ", office)

    print("\n=== Task 2: QueryBuilder ===")
    q = (QueryBuilder("users").select("id", "name").where("age > 18")
         .where("city = 'Toshkent'").order_by("name").limit(10).build())
    print(" ", q)

    print("\n=== Bonus: PizzaDirector ===")
    director = PizzaDirector(PizzaBuilder())
    print(" ", director.make_margherita())
    print(" ", director.make_pepperoni())
