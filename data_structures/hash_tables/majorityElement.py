class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        return max(m, key=m.get)