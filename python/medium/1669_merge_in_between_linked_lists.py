# https://leetcode.com/problems/merge-in-between-linked-lists/description/
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        nodeA = list1
        nodeB = list1
        for i in range(b):
            if i < a - 1:
                nodeA = nodeA.next
            nodeB = nodeB.next
        
        tail = list2
        while tail.next != None:
            tail = tail.next

        nodeA.next = list2
        tail.next = nodeB.next

        return list1
