# https://leetcode.com/problems/linked-list-cycle-ii/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        else:
            slow = head
            fast = head
            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    cycleStart = head
                    while slow and cycleStart and cycleStart != slow:
                        cycleStart = cycleStart.next
                        slow = slow.next
                    return cycleStart
            return None
