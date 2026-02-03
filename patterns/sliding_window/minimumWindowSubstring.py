class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        window = {}
        l = 0
        have = 0
        needCount = len(need)
        length = float('inf')
        res = [-1,-1]

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == needCount:
                if (r - l + 1) < length:
                    res = [l,r]
                    length = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if length != float('inf') else ""

