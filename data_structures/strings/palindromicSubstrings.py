class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPali(w, l, r):
            nonlocal res
            while r < len(w) and l >= 0 and w[l] == w[r]:
                res += 1
                l -= 1
                r +=1
            return
            
        for i in range(len(s)):
            countPali(s, i, i)
            countPali(s,i,i+1)
        
        return res 
