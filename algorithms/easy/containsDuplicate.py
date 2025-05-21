# Given:
# array nums: contains numbers
# containsDuplicate: 
#     -returns true if any values appears at least twice
#     -false if distinct

# My approach:
# make subarray
# if value in subarray return false
# otherwise return true

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sub = []
        n = len(nums)
        for i in range(n):
            if nums[i] in sub:
                return True
            sub.append(nums[i])
        return False