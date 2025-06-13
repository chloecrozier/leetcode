# https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=problem-list-v2&envId=recursion
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            curr = head
            dummy = None
            prev = dummy
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def removeNode(prev, curr):
            if curr.next:
                prev.next = curr.next
            else:
                prev.next = None
            return prev

        tail = reverseList(head)
        leftMax = tail.val
        curr = tail.next
        prev = tail
        while curr:
            if curr.val < leftMax:
                curr = removeNode(prev, curr)
            leftMax = max(leftMax, curr.val)
            prev = curr
            curr = curr.next
        
        return reverseList(tail)
