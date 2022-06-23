def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        first_num = nums[i]
        for j in range(i+1, n):
            second_num = nums[j]
            if first_num + second_num == target:
                return [i, j]
    return []
