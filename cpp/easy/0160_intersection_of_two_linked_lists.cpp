// https://leetcode.com/problems/intersection-of-two-linked-lists/description/
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        map<ListNode*, int> vals;
        while(headA != NULL){
            vals[headA] = headA->val;
            headA = headA->next;
        }
        while(headB != NULL){
            if(vals.count(headB)){
                return headB;
            }
            headB = headB->next;
        }
        return NULL;
    }
};
