from collections import Counter
from heapq import heappush, heappop, heapify


class Item(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word  # lower alpha order
        return self.freq < other.freq  # higher freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        heapify(heap)

        for key in c:
            item = Item(key, c[key])
            if len(heap) < k:
                heappush(heap, item)
            elif item > heap[0]:
                heappop(heap)
                heappush(heap, item)

        res = []

        for _ in range(k):
            res.append(heappop(heap).word)

        return res[::-1]
