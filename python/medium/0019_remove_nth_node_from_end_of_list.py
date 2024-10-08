# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        delay = 1
        prev = None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            if delay >= n:
                prev = slow
                slow = slow.next
            fast = fast.next
            delay += 1

        if delay == head or prev == None:
            return head.next
        else:
            prev.next = slow.next
            return head
