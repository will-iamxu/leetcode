/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;

        // Step 1: Find the middle of the list using slow and fast pointers
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;           // move slow by 1
            fast = fast->next->next;     // move fast by 2
        }
        // Now 'slow' is at the middle

        // Step 2: Reverse the second half of the list
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        slow->next = nullptr; // break the list into two halves

        while (curr) {
            ListNode* nextTemp = curr->next; // save next
            curr->next = prev;               // reverse current node's pointer
            prev = curr;                     // move prev forward
            curr = nextTemp;                 // move curr forward
        }
        // Now 'prev' is the head of the reversed second half

        // Step 3: Merge the two halves
        ListNode* first = head;
        ListNode* second = prev;

        while (second) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            first->next = second;    // L0 -> Ln
            second->next = tmp1;     // Ln -> L1

            first = tmp1;            // move first to L1
            second = tmp2;           // move second to Ln-1
        }
    }
};