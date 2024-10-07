# https://leetcode.com/problems/reorder-list/description/
class Solution:
    def insertNext(self, prev, new):
        temp = prev.next
        prev.next = new
        new.next = temp

    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        slow = head
        fast = head
        while fast != None and fast.next != None and slow != None:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        while curr != None:
            stack.append(curr)
            curr = curr.next
        slow.next = None
        
        curr = head
        while len(stack) > 0 and curr != None and curr.next != None:
            self.insertNext(curr, stack.pop())
            curr = curr.next.next
