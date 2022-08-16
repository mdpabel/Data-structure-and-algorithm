from heapq import heapify, heappush, heappop


heap = []

heapify(heap)

heappush(heap, 10)
heappush(heap, 11)
heappush(heap, 12)
heappush(heap, 13)
heappush(heap, 14)
heappush(heap, 5)

heappop(heap)

print(heap)
