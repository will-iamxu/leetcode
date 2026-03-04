class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        for l in range(len(nums)):
            evenSet = set()
            oddSet = set()
            for r in range(l, len(nums)):
                length = r - l + 1
                num = nums[r]
                if num % 2:
                    oddSet.add(num)
                else:
                    evenSet.add(num)
                
                if len(evenSet) == len(oddSet):
                    res = max(res, length)
        
        return res
