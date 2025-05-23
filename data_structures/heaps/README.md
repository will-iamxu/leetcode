# Heap Data Structures

Heaps are a special tree-based data structure that satisfies the heap property. In a max heap, for any given node `I`, the value of `I` is greater than or equal to the values of its children. In a min heap, the value of `I` is less than or equal to the values of its children. Heaps are commonly used to implement priority queues, where the highest (or lowest) priority element is always at the front.

## Types of Heaps

1. **Max Heap**: The parent node is always greater than or equal to its child nodes.
2. **Min Heap**: The parent node is always less than or equal to its child nodes.

## Applications of Heaps

- **Priority Queues**: Heaps are used to implement priority queues, where elements are processed based on their priority.
- **Heap Sort**: A comparison-based sorting algorithm that uses the heap data structure.
- **Graph Algorithms**: Heaps are used in algorithms like Dijkstra's and Prim's for efficiently finding the shortest path or minimum spanning tree.

## Basic Operations

- **Insertion**: Adding a new element to the heap while maintaining the heap property.
- **Deletion**: Removing the root element (max or min) and restructuring the heap.
- **Peek**: Accessing the root element without removing it.

## Example

Here is a simple example of a max heap:

```
       10
      /  \
     9    8
    / \  / \
   7  6 5   4
```

In this example, the root node (10) is greater than its children (9 and 8), satisfying the max heap property.

## Conclusion

Understanding heaps is crucial for solving various algorithmic problems efficiently. This README provides a foundational overview of heaps, their properties, applications, and basic operations. For specific implementations and problems, refer to the respective code files in this directory.

## LeetCode Problems

| Problem | Difficulty |
|---------|------------|
