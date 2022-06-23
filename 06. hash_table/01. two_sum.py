"""
nums = [3,2,4],
target = 6

map = {
    3 : 0
    2 : 1
}

required = 6 - 3 => 3
3 in map ? no

required = 6 - 2 => 4
4 in map ? no

required = 6 - 4 => 2
2 in map ? Yes


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = {}

        for i in range(n):
            required = target - nums[i]
            if required in map:
                return [i, map[required]]
            map[nums[i]] = i
