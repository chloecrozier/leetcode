# https://leetcode.com/problems/merge-two-sorted-lists/description/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head
    
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return head
