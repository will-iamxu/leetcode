# README for Hash Tables

This directory contains information and examples related to hash table data structures. Hash tables are a fundamental data structure that provides efficient key-value pair storage and retrieval. They are widely used in various applications, including databases, caches, and sets.

## Key Concepts

- **Hash Function**: A function that converts an input (or 'key') into a fixed-size string of bytes. The output is typically a hash code that is used to index the hash table.
- **Collision Resolution**: Techniques to handle situations where two keys hash to the same index in the hash table. Common methods include chaining and open addressing.
- **Load Factor**: A measure of how full the hash table is, calculated as the number of entries divided by the number of buckets. A higher load factor can lead to more collisions.

## Examples

1. **Basic Operations**:
   - Insertion
   - Deletion
   - Searching

2. **Use Cases**:
   - Implementing associative arrays
   - Caching data
   - Counting frequencies of elements

## Implementation Examples

Here's a basic example of using a hash table (unordered_map) in C++:

```cpp
#include unordered_map 
int main() {
    //declare map
    unordered_map<string, int> map(3); //all values get initalized to 0
    
    //inserting
    map["apple"] = 3; //inserts or updates
    map.insert({"banana",5}); //inserts
    
    //accessing
    cout << map["apple"]; //creates key if not present with default of 0
    cout << map.at("apple"); //throws out_of_range if not found
    
    //iterate over elements
    for (const auto& [key, value]: map){
        cout << key << ": " << value << "\n";
    }
    
    //erase key
    map.erase("apple");
    
    //size + empty
    cout << map.size();
    cout << map.empty();
    
    //clears map
    map.clear();
    
    return 0;
}
```

## LeetCode Problems

| Problem | Difficulty | Issues/Mistakes | Videos |
|---------|------------|-----------------|--------|
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/) | Easy | | |
| [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | | |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | | |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/) | Medium | | |
| [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | | |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | | |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/) | Medium | | |
| [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/description/) | Medium | | |


| [Clone Graph](https://leetcode.com/problems/clone-graph/description/) | Medium | | |## Issues
*Issues encountered while solving problems in this category (leave blank for now)*

## Videos  
*Helpful video resources for problems in this category (leave blank for now)*