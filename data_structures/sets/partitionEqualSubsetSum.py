class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            newDP = set()
            for t in dp:
                newDP.add(nums[i] + t)
                newDP.add(t)
            dp = newDP
            if target in dp:
                return True
        
        return False