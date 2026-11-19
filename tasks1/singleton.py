import threading


class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {"theme": "light", "lang": "uz"}
        return cls._instance

    def get(self, key):
        return self._settings.get(key)

    def set(self, key, value):
        self._settings[key] = value


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG] {message}")


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.connected = True
        return cls._instance


if __name__ == "__main__":
    print("=== Task 1: AppConfig ===")
    c1, c2 = AppConfig(), AppConfig()
    c1.set("theme", "dark")
    print("c2 theme:", c2.get("theme"), "| bir xil obyekt:", c1 is c2)

    print("\n=== Task 2: Logger ===")
    l1, l2 = Logger(), Logger()
    l1.log("Dastur ishga tushdi")
    l2.log("Foydalanuvchi kirdi")
    print("Jami loglar:", len(l1.logs), "| bir xil obyekt:", l1 is l2)

    print("\n=== Bonus: Thread-safe DatabaseConnection ===")
    results = []
    threads = [threading.Thread(target=lambda: results.append(id(DatabaseConnection())))
               for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("10 ta oqim, noyob obyektlar soni:", len(set(results)))
