# Given:
#     -list strs: list of strings
#     -groupAnagrams: returns list of list of grouped anagrams 
# Constraints:
#     - can be any order
#     - anagrams have to have same number of letters of each type -> frequency map
# # Approach:
# # step 1: check the map to see, notices map is empty, inserts self as value, key is number of occurances per letter 
# # step 2: check next value , insert itself as value, key is number of occurances
# # step 3: repeat for all
# # step 4: group all similar keys and return as list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {} 
        for n in strs: #for word in strings list
            count = [0] * 26 #count for frequency
            for c in n:
                idx = ord(c) - ord('a') #maps character to index
                count[idx] += 1 #increments index
            key = tuple(count) #list not hashable

            if key not in m: #if not in map, create new
                m[key] = []
            m[key].append(n) 
        return list(m.values())
        