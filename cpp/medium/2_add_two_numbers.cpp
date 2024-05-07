// https://leetcode.com/problems/add-two-numbers/
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(0);
        ListNode *iter = head;
        int overflow = 0;
        int sum = 0;
        while(l1 != NULL || l2 != NULL || overflow != 0){
            if(l1 != NULL){
                sum += l1->val;
            }
            if(l2 != NULL){
                sum += l2->val;
            }
            sum += overflow;
            overflow = sum / 10;
            iter->next = new ListNode(sum % 10);
            overflow = sum / 10;

            if(l1 != NULL){
                l1 = l1->next;
            }
            if(l2 != NULL){
                l2 = l2->next;
            }
            iter = iter->next;
            sum = 0;
        }
        return head->next;
    }
};

// // Recursive secondary solution
// class Solution {
// public:
//     void fixOverflow(ListNode *ls){
//         if(ls->next == NULL){
//             ls->next = new ListNode(1);
//         } else{
//             ls->next->val++;
//             if(ls->next->val > 9){
//                 ls->next->val = ls->next->val % 10;
//                 fixOverflow(ls->next);
//             }
//         }
//     }

//     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
//         ListNode *head = l1;
//         ListNode *iter = head;
//         int sum = 0;
//         while(iter!= NULL && l2 != NULL){
//             sum = iter->val + l2->val;
//             if(sum > 9){
//                 iter->val = sum % 10;
//                 fixOverflow(iter);
//             } else{
//                 iter->val = sum;
//             }
//             iter = iter->next;
//             l2 = l2->next;
//             sum = 0;
//         }
//         while(l2 != NULL){
//             if(iter != NULL){
//                 sum = l2->val + iter->val;
//                 if(sum > 9){
//                     iter->val = sum % 10;
//                     iter->next = new ListNode(1);
//                     iter = iter->next;
//                 } else{
//                     iter->val = sum;
//                 }
//                 l2 = l2->next;
//             } else{
//                 ListNode *temp = head;
//                 while(temp->next != NULL){
//                     temp = temp->next;
//                 }
//                 temp->next = l2;
//                 l2 = NULL;
//             }
//             sum = 0;
//         }
//         return head;
//     }
// };
