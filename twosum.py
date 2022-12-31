class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], index]
            else:
                values[value] = index