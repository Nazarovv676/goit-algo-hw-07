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

    # Функція для знаходження найбільшого значення
    def find_max(self):
        if self.root is None:
            return None  # Дерево порожнє
        return self._find_max(self.root)

    def _find_max(self, current):
        # Найбільше значення завжди в правому піддереві
        while current.right is not None:
            current = current.right
        return current.key

# Тестуємо алгоритм
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [15, 10, 20, 8, 12, 17, 25, 30]  # Значення для вставки
    for el in elements:
        bst.insert(el)

    print(f"Найбільше значення у дереві: {bst.find_max()}")