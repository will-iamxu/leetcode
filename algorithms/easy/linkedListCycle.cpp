/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Given: 
//     - listNode head: head of a singly linked list
//     - bool hasCycle: determines if list has a repeating cycle
// Constraints:
//     - if no head or no head -> next return false
//     - fast and fast->next can't be nullptr to allow for fast->next->next
// Approach:
//     - two pointers, slow and fast
//         - slow one iterates one
//         - fast iterates two
//     - if they are at the same place then the linked list has a cycle in it
//         - slow->next == fast->next->next
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head || !head->next) return false;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast!=nullptr && fast->next!=nullptr){
            slow = slow->next;
            fast = fast->next->next;
            if (slow==fast) return true;
        }
        return false;
    }
};