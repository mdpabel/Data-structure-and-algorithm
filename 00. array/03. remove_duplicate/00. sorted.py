def removeDuplicates(self, nums: List[int]) -> int:
    k = 0
    n = len(nums)
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i - 1]
            k += 1
    nums[k] = nums[n - 1]
    k += 1
    return k
