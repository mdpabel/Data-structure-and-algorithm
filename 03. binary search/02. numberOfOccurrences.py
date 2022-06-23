from bisect import bisect_left
from bisect import bisect_right

arr = [1, 1, 2, 2, 2, 2, 3, 3];

left = bisect_left(arr, 2)
right = bisect_right(arr, 2)

print(right - left)