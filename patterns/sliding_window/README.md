# Sliding Window Pattern

The sliding window pattern is a useful technique for solving problems that involve a contiguous sequence of elements in an array or list. This pattern is particularly effective for problems that require finding a subarray or substring that meets certain criteria.

## Explanation

The sliding window technique involves maintaining a window that can expand and contract as needed. The window is defined by two pointers, typically referred to as the left and right pointers. As the right pointer moves to include new elements in the window, the left pointer may move to exclude elements from the window when certain conditions are met.

## Use Cases

The sliding window pattern is commonly used in problems such as:

- Finding the maximum or minimum sum of a subarray of a fixed size.
- Finding the longest substring without repeating characters.
- Finding the smallest subarray with a sum greater than or equal to a given value.

## Examples

1. **Maximum Sum of a Subarray of Size K**
   - Given an array of integers and a number K, find the maximum sum of a subarray of size K.

2. **Longest Substring Without Repeating Characters**
   - Given a string, find the length of the longest substring without repeating characters.

3. **Smallest Subarray with a Sum Greater than or Equal to S**
   - Given an array of integers and a number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S.

## Conclusion

The sliding window pattern is a powerful tool for solving a variety of problems involving sequences. By efficiently managing the window size and position, you can often reduce the time complexity of your solutions.

## LeetCode Problems

| Problem | Difficulty |
|---------|------------|

| [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) | Medium |