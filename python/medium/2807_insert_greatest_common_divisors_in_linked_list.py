# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter = head
        while iter.next != None:
            gcd = ListNode(math.gcd(iter.val, iter.next.val))
            gcd.next = iter.next
            iter.next = gcd
            iter = gcd.next
        
        return head
