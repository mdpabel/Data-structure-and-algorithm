from calendar import isleap
from requests import head


class MinHeap:
    def __init__(self) -> None:
        self.heap = [0]
        self.heap[0] = -1
        self.front = 1

    def parent(self, idx):
        return idx // 2

    def leftChild(self, idx):
        return 2 * idx

    def rightChild(self, idx):
        return (2 * idx) + 1

    def isLeaf(self, idx):
        return idx * 2 > len(self.heap) - 1

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def heapify(self, pos):
        if not self.isLeaf(pos):
            left = self.leftChild(pos)
            right = self.rightChild(pos)

            if self.heap[left] < self.heap[right]:
                self.swap(pos, left)
                self.heapify(left)
            else:
                self.swap(pos, right)
                self.heapify(right)

    def insert(self, val):
        self.heap.append(val)

        currentIndex = len(self.heap) - 1
        parent = self.parent(currentIndex)

        while currentIndex > self.front and self.heap[currentIndex] < self.heap[parent]:
            self.swap(currentIndex, parent)
            currentIndex = parent
            parent = self.parent(parent)

    def remove(self):
        self.swap(self.front, len(self.heap)-1)
        popped = self.heap.pop()

        self.heapify(self.front)

        return popped

    def printHeap(self):
        print(self.heap[1:])


heap = MinHeap()
heap.insert(10)
heap.insert(11)
heap.insert(12)
heap.insert(13)
heap.insert(14)
heap.insert(5)

heap.remove()

heap.printHeap()
