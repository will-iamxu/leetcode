class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perm, nums, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        
        dfs([], nums, [False] * len(nums))
        return res 