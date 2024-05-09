// Posted Solution: https://leetcode.com/problems/reverse-linked-list/solutions/5137242/simple-recursive-c-approach-beats-99-time-complexity-o-n-space-complexity-o-n
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
