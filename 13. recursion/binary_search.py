def binary_search(list, left, right, key):
    if left > right:
        return -1

    mid = (left + right) // 2

    if list[mid] == key:
        return mid

    return binary_search(list, left, mid - 1, key) if list[mid] > key else binary_search(list, mid + 1, right, key)


print(binary_search([1, 2, 3, 4, 5], 0, 4, 14))
