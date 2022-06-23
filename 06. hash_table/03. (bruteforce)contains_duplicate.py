class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        1 2 3 1
        1
        1 2
        1 3
        1 1
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
                    break
        return False