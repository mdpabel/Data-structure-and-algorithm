def swap(arr, first, second):
    # temp = arr[first]
    # arr[first] = arr[second]
    # arr[second] = temp
    arr[first], arr[second] = arr[second],arr[first]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        lowest = i
        for j in range(i+1, n):
            if arr[lowest] > arr[j]:
                lowest = j
        if lowest != i:
            swap(arr, i, lowest)

li = [10,1,4,12]
selectionSort(li)
print(li)

"""
10,1,4,12

10

10* 1 4 12
10 1* 4 12 ->1
10 1* 4 12 ->1
10 1* 4 12 ->1
1 10 4 12

10
10* 4 12
10 4* 12 ->4
10 4* 12 ->4
4 10 12

10
10* 12
10* 12 -> 10


"""