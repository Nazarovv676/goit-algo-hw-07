class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Додавання вузла в дерево
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    # Функція для знаходження найменшого значення
    def find_min(self):
        if self.root is None:
            return None  # Дерево порожнє
        return self._find_min(self.root)

    def _find_min(self, current):
        # Найменше значення завжди в лівому піддереві
        while current.left is not None:
            current = current.left
        return current.key

# Тестуємо алгоритм
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [15, 10, 20, 8, 12, 17, 25, 30]  # Значення для вставки
    for el in elements:
        bst.insert(el)

    print(f"Найменше значення у дереві: {bst.find_min()}")