# Given: 
#     - string s: 
#     - int k: amount of times you can change a character
#     - characterReplacement: return longest substring of the same characters
# Constraints:
#     - longest substring given any letter is 1 + k
#     - Replace least frequent characters
# Naive Solution:
#     - two for loops
#         - outer loop loops through characters
#         - inner loop keeps track longest string given outer loop character i
# My Approach:
#     - use a sliding window and a dictionary to keep track of frequencies
# Example:
# 1) ABAB -> A -> dict["A"] = 1, n = 1, k =2
# 2) BAB -> B -> dict["B"] = 1 since k = 2, k-1 and add 1 to length, n = 2, k =1
# 3) AB -> A -> dict["A"] += 1 = 2, n =3, k = 1 
# 4) B -> dict["B"] += 1 = 2, n = 4, k = 0


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        d = {}
        maxf = 0
        for r in range(len(s)):
            curr = s[r]
            d[curr] = 1 + d.get(curr, 0)
            maxf=max(maxf, d[curr])
            if (r-l+1) - maxf > k:
                d[s[l]] -=1
                l += 1
            res = max(res, r-l+1)
        return res
                    
