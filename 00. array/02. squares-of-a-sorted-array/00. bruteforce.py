def sortedSquares(nums: List[int]) -> List[int]:
    sorted_sq = []

    for num in nums:
        sorted_sq.append(num * num)
    sorted_sq.sort()
    return sorted_sq
