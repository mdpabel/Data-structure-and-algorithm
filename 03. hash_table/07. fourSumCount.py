"""
[1, 2]
[-2,-1]

-1
0
0
1

[-1, 2]
[0, 2]

-1
1
2
4

[-1,-1]
[-1,1]

-2, 0, -2, 0
{
    -2 : 2
    0 : 2
}


[-1,1]
[1,-1]

0, -2, 2, -2


"""
from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)

        map = defaultdict(int)

        for i in range(n):
            for j in range(n):
                sum = nums1[i] + nums2[j]
                map[sum] += 1

        count = 0
        for i in range(n):
            for j in range(n):
                sum = (nums3[i] + nums4[j]) * -1
                if sum in map:
                    count += map[sum]
        print(map)
        return count