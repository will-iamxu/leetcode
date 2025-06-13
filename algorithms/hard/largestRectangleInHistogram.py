# Given:
#     - array int heights: heights[i] is height at i
#     - largestRectangleArea: returns largest rectangle created given heights
# Constraints:
#     - area = width * height
#         - width: each bar is width 1
#         - height: minHeight from index n to i
# Brute Force:
#     - double loop to count max area
#     - first loop: i, second loop starts at i + 1, and a minHeight variable to hold
#     - min(heights[i], minheight) * j - i + 1 = area



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height*(i-idx))
                start = idx
            stack.append((start, h))

        for i, h, in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
