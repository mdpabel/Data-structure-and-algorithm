"""
    nums = [2,11,15,7],
    target = 9

    2
    2 + 11 ? NO
    2 + 15 ? NO
    2 + 7 ? YES

    nums = [3,2,4],
    target = 6

    3
    3 + 2 ? NO
    3 + 4 ? NO
    2
    2 + 4 ? Yes
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]