# Binary Search Pattern

The binary search pattern is a fundamental algorithmic technique used to efficiently search for a target value within a sorted array or list. This pattern significantly reduces the time complexity of search operations compared to linear search methods.

## Explanation

Binary search works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the search continues in the lower half. Otherwise, it continues in the upper half. This process continues until the value is found or the interval is empty.

## Time Complexity

- **Best Case:** O(1) - The target value is found at the middle of the array.
- **Average Case:** O(log n) - The search space is halved with each iteration.
- **Worst Case:** O(log n) - The search space is halved until the target is found or the interval is empty.

## Examples

1. **Finding an Element in a Sorted Array**
   - Given a sorted array and a target value, implement a function to return the index of the target value or -1 if not found.

2. **Finding the First or Last Position of an Element**
   - Given a sorted array and a target value, implement a function to find the first and last position of the target value.

3. **Searching in Rotated Sorted Array**
   - Given a rotated sorted array, implement a function to search for a target value.

## Implementation

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Conclusion

The binary search pattern is a powerful technique that can be applied to various problems involving sorted data. Understanding and mastering this pattern is essential for efficient algorithm design and problem-solving in competitive programming and technical interviews.

## LeetCode Problems

| Problem | Difficulty | Issues/Mistakes | Videos |
|---------|------------|-----------------|--------|
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | | |
| [Search A 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/) | Medium | | |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/) | Medium | | |
| [Find Minimum In Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) | Medium | | |
| [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | | |
| [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/description/) | Medium | | |

## Issues
*Issues encountered while solving problems in this category (leave blank for now)*

## Videos  
*Helpful video resources for problems in this category (leave blank for now)*