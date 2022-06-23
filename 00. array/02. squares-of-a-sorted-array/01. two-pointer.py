def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums) - 1
    p1 = 0
    p2 = n
    sq_arr = [0 for _ in range(n + 1)]

    while p1 != p2:
        if abs(nums[p1]) > abs(nums[p2]):
            sq_arr[n] = abs(nums[p1] * nums[p1])
            p1 += 1
        else:
            sq_arr[n] = abs(nums[p2] * nums[p2])
            p2 -= 1
        n -= 1
    sq_arr[n] = abs(nums[p2] * nums[p2])

    return sq_arr
