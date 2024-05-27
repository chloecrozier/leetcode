// Posted Solution: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/5214049/simple-iterative-c-approach-beats-100-of-times/
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *iter = head;
        int length = 0;
        while(iter != NULL){
            iter = iter->next;
            length++;
        }
        if(length == n){
            return head->next;
        }
        ListNode *prev = head;
        iter = head;
        while(iter != NULL){
            prev = iter;
            iter = iter->next;
            length--;
            if(length == n){
                prev->next = iter->next;
                return head;
            }
        }
        return NULL;
    }
};
