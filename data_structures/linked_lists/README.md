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

### Example Implementation

Here is a simple implementation of a singly linked list in c++:

```cpp
struct Node{
    int data; //value
    Node* next; //pointer to next node
    Node(int val) : data(val), next(nullptr) {}
}
struct LinkedList {
    Node* head;
    Node* tail;
    LinkedList() : head(nullptr), tail(nullptr) {}
}
void insertAtBeginning(Node*& head, int val){
    Node* newNode = new Node(val); 
    newNode->next = head; //whats after newNode is head
    head = newNode; //head is now newNode
}
void insertAtEnd(Node*& head, int val){ //no tail
    Node* newNode = new Node(val);
    if (!head){
        head = newNode; //if theres no head, newNode is head
        return;
    }
    Node* temp = head;
    while (temp->next) temp = temp->next; //if no tail node, has to traverse to end of list to add to end
    temp->next = newNode;
}

void insertAtEndTail(int val){ //with tail
    Node* newNode = new Node(val); 
    tail->next = newNode; //last value is newNode
    tail = newNode;
}

void insertAtPosition(Node*& head, int val, int pos){
    Node* newNode = new Node(val);
    Node* temp = head;
    for (int i = 0; i<pos-1; ++i){ //stop one node before insert
        temp = temp -> next;
    }
    newNode->next = temp->next; //point newNode to what comes after temp
    temp->next=newNode; //points temp to newNode
}

void deleteByValue(Node*& head, int val) {
    if (!head) return;
    if (head->data == val) {
        Node* toDelete = head;
        head = head->next;
        delete toDelete;
        return;
    }
    Node* temp = head;
    while (temp->next && temp->next->data != val) temp = temp->next;
    if (temp->next) {
        Node* toDelete = temp->next;
        temp->next = temp->next->next;
        delete toDelete;
    }
}

void deleteAtPosition(Node*& head, int pos) {
    if (!head) return;
    if (pos == 0) {
        Node* toDelete = head;
        head = head->next;
        delete toDelete;
        return;
    }
    Node* temp = head;
    for (int i = 0; i < pos - 1 && temp->next; i++) temp = temp->next;
    if (temp->next) {
        Node* toDelete = temp->next;
        temp->next = temp->next->next;
        delete toDelete;
    }
}

bool search(Node* head, int val) {
    while (head) {
        if (head->data == val) return true;
        head = head->next;
    }
    return false;
}

void reverse(Node*& head) {
    Node* prev = nullptr;
    Node* curr = head;
    Node* next = nullptr;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head = prev;
}

int count(Node* head) {
    int cnt = 0;
    while (head) {
        cnt++;
        head = head->next;
    }
    return cnt;
}
```

### Use Cases

Linked lists are commonly used in scenarios where dynamic memory allocation is required, such as:

- Implementing stacks and queues
- Managing memory in applications
- Creating adjacency lists for graphs

### Conclusion

Linked lists are a fundamental data structure that provides flexibility in memory management and efficient data manipulation. Understanding linked lists is crucial for solving various algorithmic problems on platforms like LeetCode.

## LeetCode Problems

| Problem | Difficulty | Issues/Mistakes | Videos |
|---------|------------|-----------------|--------|
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | | |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | | |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | | |
| [Reorder List](https://leetcode.com/problems/reorder-list/description/) | Medium | | |
| [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | | |


| [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/) | Medium | | |## Issues
*Issues encountered while solving problems in this category (leave blank for now)*

## Videos  
*Helpful video resources for problems in this category (leave blank for now)*