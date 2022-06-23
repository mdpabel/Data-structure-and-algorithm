def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        expected_num = target - nums[i]
        if expected_num in hash_table:
            return [hash_table.get(expected_num), i]
        else:
            hash_table[nums[i]] = i
    return []
