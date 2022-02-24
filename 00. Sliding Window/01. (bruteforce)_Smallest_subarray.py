"""
sum >= 8
1 3 5 3 8 1 5 3 1 8 1 4

1 3 5 size = 3
  3 5 size = 2
    5 3 size = 2
      3 8 size = 2
        8 size = 1 return
"""

import math

def smallestSub(li, sum):
    n = len(li)

    smallestSize = math.inf
    for i in range(n):
        currentSum = 0
        for j in range(i, n):
            currentSum += li[j]
            if(currentSum >= sum):
                smallestSize = min(smallestSize, j - i + 1)
                break
            if(smallestSize == 1):
                return 1
    return smallestSize

li = [1, 3, 5, 3, 8, 1, 5, 3, 1, 8, 1, 4]
k = 8

res = smallestSub(li, k)
print(res)