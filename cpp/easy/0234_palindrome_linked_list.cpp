// https://leetcode.com/problems/palindrome-linked-list/description/
class Solution {
public:
    ListNode* temp;
    bool isEqual(ListNode* head){
        if(head == NULL){
            return true;
        }
        bool equal = isEqual(head->next) && (temp->val == head->val);
        temp = temp->next;
        return equal;
    }

    bool isPalindrome(ListNode* head) {
        temp = head;
        return isEqual(head);
    }
};
