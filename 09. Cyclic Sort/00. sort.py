""" The time complexity of the above algorithm is O(n). Although we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop, but in the worst-case scenario, the while loop will swap a total of n-1 numbers, and once a number is at its correct index, we will move on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1) which is asymptotically equivalent to O(n)
"""


def cyclic_sort(arr):
    i, n = 0, len(arr)

    while i < n:
        print()
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr


def main():
    print(cyclic_sort([3, 0, 1, 2]))


main()

"""
3, -2, 0, 1, 2
0 -2 3 1 2

"""
