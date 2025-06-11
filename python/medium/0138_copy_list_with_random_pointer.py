# https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        i = 0
        curr = head
        while curr:
            m[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                m[curr].next = m[curr.next]
            else:
                m[curr].next = None

            if curr.random:
                m[curr].random = m[curr.random]
            else:
                m[curr].random = None

            curr = curr.next

        if head:
            return m[head]
        else:
            return None
