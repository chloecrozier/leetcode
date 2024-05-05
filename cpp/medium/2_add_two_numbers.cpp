// https://leetcode.com/problems/add-two-numbers/
class Solution {
public:
    ListNode* addOverflow(ListNode *ls){
        ls->val = ls->val%10;
        ListNode *head = ls;
        while(ls->next != NULL){
            if(ls->next->val > 9){
                ls->val = ls->val%10;
                ls = ls->next;
            } else {
                ls->val += 1;
            }
        } else{
            ls = new ListNode(1);
        }
        return head;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *res = NULL;
        int sum = 0;
        while(l1 != NULL || l2 != NULL){
            if(l1 != NULL){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL){
                sum += l2->val;
                l2 = l2->next;
            }
            res = new ListNode(sum, res);
            if(sum > 9){
                res = addOverflow(res);
            }
            sum = 0;
        }
        return res;
    }
};
