# Given:
#     - array int nums
#     - findMin returns minimum element of the array
# Constraints:
#     - rotating an array: [a[0], a[1], a[2]... a[n-1]] rotateted once is [a[n-1], a[0], a[1]... a[n-2]]
#     - O(log n) time
# Brute force approach:
#     - loop through array, keep track of smallest number
# An Optimized look:
#     - Binary search:
#         - while left < right
#         - mid = left+right//2 
#             - if nums[right] < nums[mid] -> left = mid+1
#             - if nums[right] > nums[mid] -> right = mid
# Worked through examples
# [4,5,6,7,0,1,2]
# 0) left = 0, right = len(nums) - 1
# 1) nums[left] = 4, nums[right] = 2, mid = 0 + 6 // 2 = 3, nums[mid] = 7
# 2) since nums[mid] > nums[right] -> left = 4
# 3) nums[left] = 0, nums[right] = 2, mid = 5, nums[mid] = 1
# 3) since nums[mid] < nums[right] -> right = mid = 5
# 4) nums[left] = 0, nums[right] = 1, mid = 4, nums[mid] = 0
# 5) since nums[mid] < nums[right] -> right = mid = 4
# 6) loop exits because left == right, return nums[left]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
    
        return nums[left]