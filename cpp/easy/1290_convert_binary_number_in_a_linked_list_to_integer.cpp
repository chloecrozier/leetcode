// Posted Solution: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solutions/5137431/simple-c-bit-shifting-solution
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int num = 0;
        while(head != NULL){
            num = (num << 1) + head->val;
            head = head->next;
        }
        return num;
    }

    // int getIndex(ListNode* head){
    //     if(head->next == NULL){
    //         return 0;
    //     }
    //     return 1 + getIndex(head->next);
    // }

    // int getDecimalValue(ListNode* head) {
    //     int power = getIndex(head);
    //     int num = 0;
    //     while(head != NULL){
    //         if(head->val == 1){
    //             num += pow(2, power);
    //         }
    //         head = head->next;
    //         power--;
    //     }
    //     return num;
    // }
};
