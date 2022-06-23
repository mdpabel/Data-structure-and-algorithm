def marge(arr, left, mid, right):
    temp = []

    i, j = left, mid+1

    while mid >= i and right >= j:
        if arr[i] > arr[j]:
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1

    while mid >= i:
        temp.append(arr[i])
        i += 1

    while right >= j:
        temp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]


def merge_sort(arr, left, right):

    if(left >= right):
        return

    mid = left + (right - left) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    marge(arr, left, mid, right)


arr = [10, 11, 2, 3, 1]
merge_sort(arr, 0, 4)

print(arr)
