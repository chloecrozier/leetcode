// https://leetcode.com/problems/odd-even-linked-list/
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL){
            return head;
        }
        ListNode* odd = head;
        ListNode* evenStart = head->next;
        ListNode* even = evenStart;

        while(even != NULL && even->next != NULL){
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenStart;
        return head;
    }
};
