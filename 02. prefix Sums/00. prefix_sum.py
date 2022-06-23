def prefix_sum(arr, n, prefix_sum_arr):
    prefix_sum_arr[0] = arr[0]

    for i in range(1, n):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i]


arr = [10, 20, 10, 5, 15]
n = len(arr)
prefix_sum_arr = [0 for _ in range(n)]

prefix_sum(arr, n, prefix_sum_arr)

print(prefix_sum_arr)
