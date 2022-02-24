"""
[1,2,3,1,1,3]
1
1 2
1 3
1 1 -y
1 1 -y
1 3 -y

hash :
map = {

}
1 : [0, 3, 4] -> (n-1)*n/2
2 : [1]
3 : [2, 5]
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        map = {}

        for i in range(n):
            if nums[i] not in map:
                map[nums[i]] = []
            map[nums[i]].append(i)

        count = 0
        for item in map:
            n = len(map[item])
            pairs = ((n-1) * n) //2
            count += pairs
        return count
