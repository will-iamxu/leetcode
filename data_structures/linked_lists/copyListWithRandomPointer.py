"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current = head
        while current:
            copy = Node(current.val)  # Create a copy of the current node
            copy.next = current.next  # The new copy points to the next original node
            current.next = copy  # Link the original node to the copy node
            current = copy.next  # Move to the next original node

        # Step 2: Set the random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next  # Set the random pointer for the copy
            current = current.next.next  # Move to the next original node

        # Step 3: Separate the original list and the copied list
        current = head
        new_head = head.next  # The new head is the first copied node
        while current:
            copy = current.next
            current.next = copy.next  # Restore the next pointer of the original list
            if copy.next:
                copy.next = copy.next.next  # Set the next pointer for the copied list
            current = current.next  # Move to the next original node

        return new_head  # Return the head of the copied list