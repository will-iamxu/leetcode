# This file contains information and examples related to linked list data structures.

## Linked Lists

A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for efficient insertions and deletions.

### Types of Linked Lists

1. **Singly Linked List**: Each node contains data and a pointer to the next node.
2. **Doubly Linked List**: Each node contains data, a pointer to the next node, and a pointer to the previous node.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

### Basic Operations

- **Insertion**: Adding a new node to the list.
- **Deletion**: Removing a node from the list.
- **Traversal**: Accessing each node in the list.
- **Searching**: Finding a node with a specific value.

### Example

Here is a simple implementation of a singly linked list in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

### Use Cases

Linked lists are commonly used in scenarios where dynamic memory allocation is required, such as:

- Implementing stacks and queues
- Managing memory in applications
- Creating adjacency lists for graphs

### Conclusion

Linked lists are a fundamental data structure that provides flexibility in memory management and efficient data manipulation. Understanding linked lists is crucial for solving various algorithmic problems on platforms like LeetCode.