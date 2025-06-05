// Given: 
//     -ListNode* head: head of a linked list
//     - int n
//     - removeNthFromEnd: remove the nth node from the end of a linked list
// Constraints:
//     - head needs to exist (!head -> return)
// Approach:
//     - Count size of linked list
//         - temp variable to go through list and a counting variable, length, to count
//     - delete length - n node

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        int length = 1;
        while(temp->next!=nullptr){
            temp = temp->next;
            ++length;
        }
        int pos = length - n;
        if (pos == 0){
            ListNode* toDelete = head;
            head = head->next;
            delete toDelete;
            return head;
        }
        temp = head;
        for (int i = 0; i<pos -1 && temp->next; ++i) temp = temp->next;
        if (temp->next) {
            ListNode* toDelete = temp->next;
            temp->next = temp->next->next;
            delete toDelete;
        }
        return head;
    }
};