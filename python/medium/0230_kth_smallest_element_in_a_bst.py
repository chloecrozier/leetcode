# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        visit = [root]
        while visit:
            curr = visit.pop(0)
            if curr:
                heapq.heappush(pq, curr.val)
                visit.append(curr.left)
                visit.append(curr.right)

        for i in range(k - 1):
            heapq.heappop(pq)

        return heapq.heappop(pq)
