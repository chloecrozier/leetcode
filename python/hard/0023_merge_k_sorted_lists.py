# https://leetcode.com/problems/merge-k-sorted-lists/description/
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count = {}
        for l in lists:
            curr = l
            while curr != None:
                if curr.val in count:
                    count[curr.val] += 1
                else:
                    count[curr.val] = 1
                print(curr.val)
                curr = curr.next

        count = dict(sorted(count.items()))
        head = ListNode(0)
        curr = head
        for key, value in count.items():
            for i in range(value):
                curr.next = ListNode(key)
                curr = curr.next
        return head.next
