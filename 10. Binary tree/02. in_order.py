class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return repr(self.data)

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node


def create_tree():
    root = Node()
    root.data = 1

    seven = Node(2)
    nine = Node(3)
    root.add_left(seven)
    root.add_right(nine)

    one = Node(4)
    six = Node(5)
    seven.add_left(one)
    seven.add_right(six)

    eight = Node(6)
    nine.add_right(eight)

    five = Node(7)
    ten = Node(8)
    six.add_left(five)
    six.add_right(ten)

    three = Node(9)
    four = Node(10)
    eight.add_left(three)
    eight.add_right(four)

    return root


def in_order(root):
    if root.left:
        in_order(root.left)
    print(root, end="->")
    if root.right:
        in_order(root.right)


if __name__ == "__main__":
    root = create_tree()
    in_order(root)
