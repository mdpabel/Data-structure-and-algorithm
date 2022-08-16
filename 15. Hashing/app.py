class HashEntry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.val = value
        self.next = None


class HashTable:
    def __init__(self) -> None:
        self.slots = 10
        self.size = 0
        self.bucket = [None] * self.slots

    def get_index(self, key):
        hashCode = hash(key)
        return hashCode % self.slots

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0
