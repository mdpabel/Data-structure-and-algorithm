class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        4,3,2,7,8,2,3,1

        7,3,2,4,8,2,3,1
        3,3,2,4,8,2,7,1
        2,3,3,4,8,2,7,1

        """
        i, n = 0, len(nums)

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        duplicates = []

        for i in range(n):
            if nums[i] != i+1:
                duplicates.append(nums[i])

        return duplicates
