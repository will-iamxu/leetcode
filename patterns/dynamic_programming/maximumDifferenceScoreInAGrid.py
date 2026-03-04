class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[float('inf')] * col for _ in range(row)]
        res = float('-inf')

        for i in range(row):
            for j in range(col):
                if i > 0:
                    top = dp[i-1][j]
                else:
                    top = float('inf')
                
                if j > 0:
                    left = dp[i][j-1]
                else:
                    left = float('inf')
                
                minPrev = min(top, left)

                if minPrev != float('inf'):
                    res = max(res, grid[i][j] - minPrev)
                
                dp[i][j] = min(minPrev, grid[i][j])
        
        return res 