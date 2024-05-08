// https://leetcode.com/problems/remove-linked-list-elements/description/
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(head == NULL){
            return NULL;
        }

        ListNode* start = new ListNode();
        start->next = head;
        ListNode* curr = start;

        while(curr->next != NULL){
            if(curr->next->val == val){
                curr->next = curr->next->next;
            } else{
                curr = curr->next;
            }
        }
        return start->next;
    }
};
