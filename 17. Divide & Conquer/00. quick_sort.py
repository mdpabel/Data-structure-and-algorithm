def partition(nums, start, end):
    i = start
    pivot = nums[end]

    for j in range(start, end):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[end] = nums[end], nums[i]
    return i


def quickSort(nums, start, end):
    if start >= end:
        return

    p = partition(nums, start, end)
    quickSort(nums, start, p-1)
    quickSort(nums, p+1, end)


nums = [5, 3, 7, 2, 6, 43, 2, 6]
quickSort(nums, 0, len(nums)-1)

print(nums)

nums = [2]
quickSort(nums, 0, len(nums)-1)

print(nums)
