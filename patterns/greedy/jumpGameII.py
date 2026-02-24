class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            high = 0
            for i in range(l, r + 1):
                high = max(high, i + nums[i])
            
            l = r + 1
            r = high
            res +=1
        
        return res 