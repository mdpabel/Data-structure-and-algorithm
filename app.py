class weight:
    def __init__(self, weight):
        self. weight = weight

    def __lt__(self, other):
        print(self.weight)
        return self.weight < other.weight


a = weight(50)
b = weight(60)
print(a > b)
