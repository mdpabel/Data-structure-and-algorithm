def twoSum(self, nums: List[int], target: int) -> List[int]:
    sorted_nums = sorted(nums)
    res = []

    left = 0
    right = len(sorted_nums) - 1

    while right >= left:
        _sum = sorted_nums[left] + sorted_nums[right]
        if _sum == target:
            break
        elif _sum > target:
            right -= 1
        else:
            left += 1
    for i in range(len(nums)):
        if nums[i] == sorted_nums[left]:
            res.append(i)
            break
    for j in reversed(range(len(nums))):
        print(j)
        if nums[j] == sorted_nums[right]:
            res.append(j)
            break
    return res
