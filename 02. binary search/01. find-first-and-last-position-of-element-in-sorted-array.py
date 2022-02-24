"""
5,7,7,8,8,10
n = 6
first = 0
last = 6
mid = 0 + 6 // 2 = 3
nums[mid] == 8 ?
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first = 0
        last = n - 1

        while first <= last:
            mid = first + ((last - first) // 2)

            if nums[mid] == target:
                i = 0
                while mid + i + 1 < n and nums[mid + i + 1] == target:
                    i += 1

                j = 0
                while mid - j-1 >= 0 and nums[mid - j-1] == target:
                    j += 1

                return [mid-j, mid+i]

            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1

        return [-1, -1]
