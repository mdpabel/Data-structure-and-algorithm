"""
12, 11, 13, 5, 6

11
11 12 13 5 6
13
11 12 13 5 6
5
5 11 12 13 6
6
5 6 11 12 13
"""

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        selected_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > selected_item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = selected_item

li = [12, 11, 13, 5, 6]
insertionSort(li)
print(li)
