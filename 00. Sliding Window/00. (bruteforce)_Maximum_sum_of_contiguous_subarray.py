"""
10 1 3 4 5 6 1 5 0 25 7
10 1 3
   1 3 4
     3 4 5
       4 5 6
         5 6 1
           6 1 5
             1 5 0
               5 0 25
                 0 25 7
"""
import math

def maxSum(li, k):
    n = len(li)
    _max = -math.inf
    for i in range(n - k + 1):
        currentSum = 0
        for j in range(i, k + i):
            currentSum += li[j]
        _max = max(currentSum, _max)
    return _max


li = [10, 1, 3, 4, 5, 6, 1, 5, 0, 25, 7]
k = 3

res = maxSum(li, k)
print(res)