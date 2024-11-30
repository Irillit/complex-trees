from typing import Optional


RED = "red"
BLACK = "black"


class Node:
    def __init__(self, data):
        self.data: int = data
        self.color: str = RED
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None


class RedBlackTree:

    def __init__(self):
        self._nil = Node(0)
        self._nil.color = BLACK
        self._nil.right = self._nil
        self._nil.left = self._nil.right

        self._root: Optional[Node] = self._nil

    def insert(self, data: int):
        new_node = Node(data)
        new_node.left = self._nil
        new_node.right = self._nil

        # BST insert
        current = self._root
        parent = None
        while current is not self._nil:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if not parent:
            self._root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if not new_node.parent:
            new_node.color = BLACK
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node: Node):
        while node is not self._root and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
        self._root.color = BLACK

    def left_rotate(self, x: Node):
        y = x.right
        x.right = y.left

        if y.left is not self._nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: Node):
        y = x.left
        x.left = y.right

        if y.right is not self._nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, data: int):
        return self._search(self._root, data)

    def _search(self, current: Node, data: int):
        if current == self._nil:
            return False
        if current.data == data:
            return True
        elif data > current.data:
            return self._search(current.right, data)
        elif data < current.data:
            return self._search(current.left, data)

    def _traverse(self, current: Node, i: int):
        if current is self._nil:
            return
        i = i + 1
        self._traverse(current.left, i)
        spaces = "  " * i
        print(f"{spaces}{current.data} {current.color}")
        self._traverse(current.right, i)

    def traverse(self):
        self._traverse(self._root, 0)


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(8)
    tree.insert(2)
    tree.insert(10)
    tree.insert(11)
    tree.insert(12)
    tree.insert(18)
    tree.insert(23)
    tree.insert(27)

    tree.traverse()

    print(tree.search(18))
    print(tree.search(45))
