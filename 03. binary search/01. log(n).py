def binarySearch(nums, target, first, last):

    while first <= last:
        mid = first + ((last - first) // 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            last = mid - 1
        else:
            first = mid + 1
    return -1

class Solution:
    def searchRange(self, nums, target):
        mid = binarySearch(nums, target, 0, len(nums) - 1)

        res = [-1, -1]
        left = mid
        right = mid

        while left != -1 :
            res[0] = left
            left = binarySearch(nums, target, 0, left - 1)

        while right != -1:
            res[1] = right
            right = binarySearch(nums, target, right + 1, len(nums) - 1)

        return res