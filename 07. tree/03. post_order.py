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

    two = Node(2)
    three = Node(3)
    root.add_left(two)
    root.add_right(three)

    four = Node(4)
    five = Node(5)
    two.add_left(four)
    two.add_right(five)

    six = Node(6)
    three.add_right(six)

    seven = Node(7)
    eight = Node(8)
    five.add_left(seven)
    five.add_right(eight)

    nine = Node(9)
    ten = Node(10)
    six.add_left(nine)
    six.add_right(ten)

    return root


def post_order(root):
    if root.left:
        post_order(root.left)
    if root.right:
        post_order(root.right)
    print(root, end="->")


if __name__ == "__main__":
    root = create_tree()
    post_order(root)
