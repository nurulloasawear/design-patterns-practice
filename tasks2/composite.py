from abc import ABC, abstractmethod


class FileSystemItem(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def show(self, indent=0): ...


class File(FileSystemItem):
    def __init__(self, name, size_kb):
        super().__init__(name)
        self._size = size_kb

    def size(self):
        return self._size

    def show(self, indent=0):
        print("  " * indent + f"- {self.name} ({self._size} KB)")


class Folder(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.children: list[FileSystemItem] = []

    def add(self, *items):
        self.children.extend(items)
        return self

    def remove(self, item):
        self.children.remove(item)

    def size(self):
        return sum(c.size() for c in self.children)

    def show(self, indent=0):
        print("  " * indent + f"+ {self.name}/ ({self.size()} KB)")
        for c in self.children:
            c.show(indent + 1)


if __name__ == "__main__":
    print("=== Composite ===")
    root = Folder("loyiha").add(
        File("README.md", 4),
        Folder("src").add(File("main.py", 12), File("utils.py", 8),
                          Folder("models").add(File("user.py", 6))),
        Folder("rasmlar").add(File("logo.png", 120)),
    )
    root.show()
    print("Jami hajm:", root.size(), "KB")
