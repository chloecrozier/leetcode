// https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* iter = head;

        while(iter != NULL && iter->next != NULL){
            if(iter->val == iter->next->val){
                iter->next = iter->next->next;
            } else{
                iter = iter->next;
            }
        }

        return head;
    }
};
