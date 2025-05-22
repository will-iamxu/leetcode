# Given:
#     - array nums: integers
#     - int k: how many things to return 
# Approach:
#     - frequency map to count elements
#     - array length k holding most frequent elememts
#     - sort by frequency

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        sol = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        items = []
        for key in d:
            items.append((key, d[key]))
        n = len(items)
        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if items[j][1] > items[idx][1]:
                    idx = j
            items[i], items[idx] = items[idx], items[i]
        result = []
        for i in range(k):
            result.append(items[i][0])
        return result


