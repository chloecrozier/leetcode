# https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=recursion
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            first = head
            second = head.next
            temp = second.next
            second.next = first
            first.next = self.swapPairs(temp)
            return second
