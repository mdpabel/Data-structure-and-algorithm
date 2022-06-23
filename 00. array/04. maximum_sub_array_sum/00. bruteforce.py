def generateSubArray(array):
    n = len(array)

    sub_arrs = []

    for l in range(1, n+1):
        for i in range(n - l + 1):
            sub_arrs.append(sum(array[i:l+i]))
    return sub_arrs


def maxSubArray(self, nums: List[int]) -> int:
    return max(generateSubArray(nums))
