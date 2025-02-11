# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = head
        curr = head
        currSum = 0
        while curr:
            if curr.val == 0:
                if currSum:
                    end.val = currSum
                    start.next = end
                    start = end
                    currSum = 0
                else:
                    temp = curr
            else:
                currSum += curr.val
            curr = curr.next
            end = end.next

        return head.next
