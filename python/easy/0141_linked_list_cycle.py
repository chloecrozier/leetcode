# https://leetcode.com/problems/linked-list-cycle/description/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
