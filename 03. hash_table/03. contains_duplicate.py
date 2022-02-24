"""
    1 2 3 1
    1
    1 2
    1 3
    1 1
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        map = {}
        for i in range(n):
            if nums[i] in map:
                return True
            else:
                map[nums[i]] = True
        return False