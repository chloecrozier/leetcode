# https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=recursion
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            dummy = ListNode(-1)
            dummy.next = head
            prev = dummy
            first = head
            second = head.next
            while first and second:
                prev.next = second
                if second:
                    first.next = second.next
                else:
                    first.next = None
                second.next = first

                prev = first
                first = first.next
                if first:
                    second = first.next
                else:
                    second = None

            return dummy.next
