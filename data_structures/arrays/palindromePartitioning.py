class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, curr):
            if i>=len(s):
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j+1, curr)
                    curr.pop()
        
        dfs(0, [])
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True