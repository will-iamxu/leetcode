# Given:
#     -string s: word or letters
#     -string t: word or letters
#     -bool isAnagram: returns true if anagram, returns false if not

# Approach: 
# 1) use a frequency map to map letters and their frequency
# 2) if maps are equal, than it is a anagram -> return True, else False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        dict1 = {}
        dict2 = {}
        n = len(s) 
        for i in range(n):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else: 
                dict1[s[i]] = 1
            if t[i] in dict2:
                dict2[t[i]] += 1
            else: 
                dict2[t[i]] = 1
        return dict1 == dict2 