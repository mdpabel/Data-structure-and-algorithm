def maxSubArray(self, nums: List[int]) -> int:
    """ 
    -2,1,-3,4,-1,2,1,-5,4

    l = -2
    c = 1
    l = 1
    c = 1 - 3 = -2
    c = 0
    c = 4
    l = 4
    c = 4 - 1 = 3
    c = 3 + 2 = 5
    l = 5
    c = 5 + 1
    l = 6
    c = 6 - 5 = 1
    c = 1 + 5
    """
    n = len(nums)
    largest_sum = nums[0]
    current_sum = largest_sum

    for i in range(1, n):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[i]
        if current_sum > largest_sum:
            largest_sum = current_sum
    return largest_sum
