"""
10 1 3 4 5 6 1 5 0 25 7
10 1 3 => 14
   1 3 4 => 14 - 10 + 4 = 8
     3 4 5 => 8 - 1 + 5
       4 5 6 =>
         5 6 1
           6 1 5
             1 5 0
               5 0 25
                 0 25 7

windowSum - arr[i] + arr[i + k]
"""
def maxSum(li, k):
    n = len(li)
    windowSum = 0
    for i in range(k):
        windowSum += li[i]

    _maxSum = windowSum

    for i in range(n - k):
        windowSum =  windowSum - li[i] + li[i + k]
        _maxSum = max(_maxSum, windowSum)

    return _maxSum

li = [10, 1, 3, 4, 5, 6, 1, 5, 0, 25, 7]
k = 3

res = maxSum(li, k)
print(res)