class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def unshift(self, val):
        """
        H:[head|A]-->A:[|B]-->B:[|null]
        D:[newNode|]

        newNode.next = head
        head = newNode

        H:[head|D]-->D:[newNode|A]-->A:[|B]-->B:[|null]
        """
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1

    def push(self, val):
        """
        H:[head|A]-->A:[|B]-->B:[|null]
        D:[newNode|]

        newNode.next = None
        tail.next = newNode
        tail = newNode
        """
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1

    def insert(self, val, position):
        """
        H:[head|A]-->A:[|B]-->B:[|null]
        D:[newNode|], 1

        newNode.next = prevNode.next
        prevNode.next = newNode
        """
        i = 0
        prevNode = self.head
        while i < position-1:
            prevNode = prevNode.next
            i += 1

        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            if self.tail == prevNode:
                self.tail= newNode
            newNode.next = prevNode.next
            prevNode.next = newNode
        self.length +=1

    def search(self, val):
        """
        H:[head|A]-->A:[|B]-->B:[|null]
        """
        node = self.head
        while node.next:
            node = node.next
            if node.value == val:
                return True
        return False

    def nthNode(self, index):
        node = self.head
        i = 0
        while node:
            if i == index:
                return node.value
            if i > index:
                return -1
            i += 1
            node = node.next







    def printf(self):
        """
        H:[head|A]-->A:[|B]-->B:[|null]
        """
        node = self.head
        if not node:
            raise Exception('The linked list is empty')
        while node:
            print(node.value)
            node = node.next
        print("HEAD-->", self.head.value, "TAIL-->",self.tail.value)










#
list = SLinkedList()

list.unshift('A')
list.unshift('B')
list.unshift('C')

list.push('D')
list.push('E')

list.insert('S', 0)
list.insert('V', 1)

print(list.search('E'))
n = list.length
print('nth-->',list.nthNode(n-1))

list.printf()