def triplet_with_smaller_sum(arr, target):
    arr.sort()
    n = len(arr)
    count = 0
     
    for i in range(n):
        count += find_pair(arr, arr[i], i + 1, target)
    return count

def find_pair(arr, first_el, left, target):
    right = len(arr) - 1
    count = 0
        
    while left < right:
        current_sum = first_el + arr[left] + arr[right]
        if current_sum < target:
            count += right - left 
            left += 1
        if current_sum > target:
            right -= 1
    return count
            

print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))

""" 
-1, 0, 2, 3

-1 + 0 + 3 
-1 + 0 + 2
-1 + 2 + 3
 0 + 2 + 3
 
"""