# Array Data Structures

This directory contains information and examples related to array data structures, which are fundamental to many algorithms and data manipulation tasks.

## Overview

Arrays are a collection of items stored at contiguous memory locations. They are used to store multiple items of the same type together. The main characteristics of arrays include:

- **Fixed Size**: The size of an array is defined at the time of declaration and cannot be changed.
- **Index-Based Access**: Elements in an array can be accessed using their index, which allows for efficient retrieval.
- **Homogeneous Elements**: All elements in an array are of the same data type.

## Common Operations

1. **Insertion**: Adding an element at a specific index.
2. **Deletion**: Removing an element from a specific index.
3. **Traversal**: Accessing each element in the array.
4. **Searching**: Finding an element in the array (linear search, binary search).
5. **Sorting**: Arranging the elements in a specific order (ascending or descending).

## Implementation Examples

```cpp
#include <array> 
#include <vector>
int main() {
    //standard c array
    //declare array of size n
    int arr[5];
    //declare array with elements
    int a[5] = {1,2,3,4,5};
    //accessing elements
    int x = a[2]; 
    //modifying elements
    a[2] = 0;
    //length 
    int len = sizeof(arr) / sizeof(arr[0]);
    
    //std::array
    array<int, 5> ar = {1,2,3,4,5};
    //accessing
    // ar.at(2);
    // ar[2];
    //modifying
    ar[2] = 50;
    ar.at(2) = 100;
    //size 
    //ar.size();
    
    //vector
    vector<int> v = {1,2,3};
    //add elements
    v.push_back(4);
    //access 
    cout << v[2];
    //modify
    v[2] = 10;
    //size
    cout << v.size();
    }
```
## Conclusion

Understanding arrays is crucial for solving many algorithmic problems on platforms like LeetCode. This directory will provide various examples and solutions to common array-related problems.

## LeetCode Problems

| Problem | Difficulty |
|---------|------------|
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/) | Easy | 
| [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | 
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/) | Medium |
| [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium |
| [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium |
| [Find Words Containing Character](https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question) | Easy |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy |
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy |
| [Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) | Medium |
| [3Sum](https://leetcode.com/problems/3sum/description/) | Medium |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/) | Medium |
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/) | Medium |
| [Search A 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/) | Medium |
| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/) | Medium |
| [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/) | Medium |