// https://leetcode.com/problems/reverse-linked-list/description/
class Solution {
public:

    ListNode* linkNext(ListNode* head, ListNode* prev){
        if(head == NULL){
            return prev;
        }
        ListNode* next = head->next;
        head->next = prev;
        return linkNext(next, head);
    }

    ListNode* reverseList(ListNode* head) {
        return linkNext(head, NULL);
    }
};
