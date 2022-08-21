from heapq import heapify, heappush, heappop


class Item():
    def __init__(self, val) -> None:
        self.val = val

    def __lt__(self, other):
        return self.val > other.val


li = [10, 3, 3, 15, 3, 7, 22, 22, 7]

heap = []

heapify(heap)

for it in li:
    item = Item(it)
    heappush(heap, item)

res = []

for _ in range(len(heap)):
    res.append(heappop(heap).val)

print(res)
