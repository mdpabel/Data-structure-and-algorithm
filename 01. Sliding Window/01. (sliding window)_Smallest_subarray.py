"""
sum >= 8
1 3 5 3 8 1 5 3 1 8 1 4
1
1 3
1 3 5 size = 3
  3 5 size = 2
    5
    5 3 size = 2
      3
      3 8 size = 2
        8 size = 1 return
"""


import math

def smallestSub(li, sum):
    n = len(li)

    smallestSize = math.inf
    windowSum = 0

    windowStart = 0
    for windowEnd in range(n):
        windowSum += li[windowEnd]

        while(windowSum >= sum):
            windowSum = windowSum - li[windowStart]
            smallestSize = min(smallestSize, windowEnd - windowStart + 1)
            windowStart += 1
        if smallestSize == 1:
            return 1
    return smallestSize

li = [1, 3, 5, 3, 8, 1, 5, 3, 1, 8, 1, 4]
k = 8

res = smallestSub(li, k)
print(res)
