from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left = Optional[Node]
        self.right = Optional[Node]
        self.height = 1


class AVL:

    def __init__(self):
        self._root: Optional[Node] = None

    def insert(self, data):
        new_node = Node(data)
        current = self._root
        parent = None

        while current is not None:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right


    def search(self):
        pass

    def delete(self):
        pass

    def traverse(self):
        pass


if __name__ == "__main__":
    tree = AVL()
