class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        currIdxParent = (len(array) - 2) // 2
        for currentIdx in reversed(range(currIdxParent + 1)):
            self.siftDown(currentIdx, array)
        return array

    def siftDown(self, currentIdx, heap):
        n = len(heap) - 1
        childOne = currentIdx * 2 + 1

        while childOne <= n:
            childTwo = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= n else -1
            if childTwo != -1 and heap[childOne] > heap[childTwo]:
                indexToSwap = childTwo
            else:
                indexToSwap = childOne

            if heap[indexToSwap] < heap[currentIdx]:
                self.swap(currentIdx, indexToSwap, heap)
                currentIdx = indexToSwap
                childOne = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        currIdxParent = (currentIdx - 1) // 2
        while currentIdx > 0 and self.heap[currentIdx] < self.heap[currIdxParent]:
            self.swap(currentIdx, currIdxParent, heap)
            currentIdx = currIdxParent
            currIdxParent = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        indexToSwap = len(self.heap) - 1
        self.swap(0, indexToSwap, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, self.heap)
