from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = defaultdict(int)

        for i in range(n):
            map[nums[i]] += 1
            if map[nums[i]] > n//2:
                return nums[i]
