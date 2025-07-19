class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break                
                curr.append(candidates[j])
                dfs(j, curr, total + candidates[j])
                curr.pop()
        
        dfs(0, [], 0)

        return res 

            
