# Given: 
#     -array nums: numbers
#     -int target: target sum
#     -twoSum: return indices of the two numbers that add up to target
# Constraints:
#     - cannot use same element twice
#     - exactly one solution
# Approach:
# 1) create a dictionary with target - index 
# 2) if result exists in nums: return indexes
    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in map:
                return [map[complement], i]
            map[n] = i
        