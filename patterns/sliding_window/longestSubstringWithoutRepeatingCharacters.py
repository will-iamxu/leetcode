# // Given:
# //     - string s
# //     - lengthOfLongestSubstring: longest substring without duplication characters
# // Constraints:
# //     - no duplicate characters 
# //         - ex. bbbbb -> b : 1
# //     - not a subsequence
# //         - ex. pwwkew -> not pwke because thats a subsequence
# // Approach:
# //     - use a sliding window and a dictionary to map most recent index of character (hashSet)
# //     - move right pointer one at a time, if character is in the set that means theres a duplicate and we need to shrink the window from the left 
# //     - if chaarcetr was seen and it inside current window move left to last seen index
# //     - have a maxLength variable to hold count
# //         - maxLength is right - left + 1
# // Pesudo Code:
# //     max = 0
# //     dict = set()
# //     left = 0
# //     for right in range len(s);
# //         while s[right] in dict:
# //             remove(s[left]) from dict
# //             left+=1 move left to next non repeating char
# //         dict.add(s[right])
# //         max(max, right-left+1)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])  
                left += 1
            charSet.add(s[right])  
            maxLength = max(maxLength, right - left + 1)
        return maxLength
        