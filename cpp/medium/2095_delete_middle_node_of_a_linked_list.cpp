// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
class Solution {
public:

    int getLength(ListNode* head){
        if(head == NULL){
            return 0;
        }
        return 1 + getLength(head->next);
    }

    ListNode* deleteMiddle(ListNode* head) {
        int mid = getLength(head) / 2, index = 0;
        ListNode* prev = head;

        for(ListNode* cur = head; cur != NULL; cur = cur->next){
            if(index == mid){
                prev->next = cur->next;
            }
            prev = cur;
            index++;
        }
        return mid > 0 ? head : NULL;
    }
};
