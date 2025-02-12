# https://leetcode.com/problems/rotate-list/description/
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k== 0 or head == None or head.next == None:
            return head

        end = head
        length = 1
        while end and end.next:
            length += 1
            end = end.next

        if k % length == 0:
            return head

        curr = head
        start = head
        index = 0
        while index < length - (k % length + 1):
            curr = curr.next
            index += 1

        head = curr.next
        end.next = start
        curr.next = None

        return head
