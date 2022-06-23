def swap(arr, first, second):
    # temp = arr[first]
    # arr[first] = arr[second]
    # arr[second] = temp
    arr[first], arr[second] = arr[second],arr[first]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = True
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                flag = False
        if flag:
            break

li = [10,10,11,1,1,2,3]

bubble_sort(li)

print(li)