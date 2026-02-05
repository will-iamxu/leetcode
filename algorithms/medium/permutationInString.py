# Given:
#     string s1:
#     string s2:
#     checkInclusion: checks if s2 is a permutation is a permutation of s1
# Constraints:
#     permutation: contains same characters but can be in different order
# Naive Approach:
#     for every char s1 
#         for every char s2
#             subtract character from s1
# Better Approach:
#     use a frequency map for s1
#     sliding window of length s1, if character in map decrement map
#     if map empty after, return true

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0] * 26
        c2 = [0] * 26
        a_ord = ord('a')

        # Pre-fill the frequency arrays for s1 and first window in s2
        for i in range(len(s1)):
            c1[ord(s1[i]) - a_ord] += 1
            c2[ord(s2[i]) - a_ord] += 1

        # Check the first window
        if c1 == c2:
            return True

        # Slide the window from index len(s1) to end of s2
        for r in range(len(s1), len(s2)):
            c2[ord(s2[r]) - a_ord] += 1                      # Add new char to right
            c2[ord(s2[r - len(s1)]) - a_ord] -= 1            # Remove char from left

            if c1 == c2:
                return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        window = {}
        for i in range(len(s1)):
            c = s2[i]
            window[c] = window.get(c, 0) + 1
        
        if window == s1Count:
            return True
        
        for r in range(len(s1), len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            l = r - len(s1)
            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                del window[s2[l]]

            if window == s1Count: return True
        
        return False
                
        