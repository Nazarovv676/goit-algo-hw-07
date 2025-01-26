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

    # Функція для знаходження суми всіх значень
    def sum_of_all_values(self):
        return self._sum_of_all_values(self.root)

    def _sum_of_all_values(self, current):
        if current is None:
            return 0
        # Рекурсивно додаємо значення поточного вузла та значення лівого і правого піддерева
        return current.key + self._sum_of_all_values(current.left) + self._sum_of_all_values(current.right)

# Тестуємо алгоритм
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [15, 10, 20, 8, 12, 17, 25, 30]  # Значення для вставки
    for el in elements:
        bst.insert(el)

    print(f"Сума всіх значень у дереві: {bst.sum_of_all_values()}")