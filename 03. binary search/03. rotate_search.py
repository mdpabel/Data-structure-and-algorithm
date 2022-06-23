"""
4,5,6,7,8,9,10,1,2,3
target

4,5,6,7,8
1,2,3

m > s:



m = 4 => 8
m > target and s < target = left
e = m - 1

s = m + 1


m < target and e > target = right
s = m + 1

e = m + 1

"""

def rotate_search(arr, key):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] >= arr[start]:
            # Left
            if arr[mid] >= key and key >= arr[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # Right
            if arr[mid] < key and key <= arr[end]:
                start = mid + 1
            else:
                end = mid -1
    return -1

print(rotate_search([2,3,4,1,2], 3))