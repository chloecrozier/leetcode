# https://leetcode.com/problems/sort-list/description/
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        curr = head
        res = []
    
        while curr != None:
            print(curr.val)
            res.append(curr.val)
            curr = curr.next
        
        res.sort()
        curr = start
        while curr != None:
            curr.val = res.pop(0)
            curr = curr.next

        return start
