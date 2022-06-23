"""
(val, min)
[(100, 100), (100, 24), (50, 24), (12,12)]
m = 100
100
24
50
12
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.mininum = float("inf")

    def push(self, val: int) -> None:
        current_min = self.getMin()
        if current_min == None or current_min > val:
            current_min = val
        self.stack.append((val,current_min))


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()