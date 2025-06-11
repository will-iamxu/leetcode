# Given:
#     -array int nums: contains n+1 in the range [1,n]
#     - findDuplicate: 1 repeated number, return this number
# Constraints:
#     - only use constant extra space
#     - can't modify list
# Brute Force:
#     - hash map, O(n) time but O(n) space
#     - loop through list, if freq > 1 return num
# Approach:
#     - Even though list, can use fast and slow pointers
#     - Floyds algorithm 
#         - Fast, slow
#         - Find first intersection
#         - Leave slow pointer at intersection
#         - Put a second slow pointer at first node 
#         - Wherever they meet is repeated number bc they traverse same distance
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s2 = 0
        while True:
            s2 = nums[s2]
            s = nums[s]
            if s == s2:
                return s
        