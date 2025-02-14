# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13
class Solution:
    def newValue(self, x, y):
        return min(x, y) * 2 + max(x, y)

    def minOperations(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)

        count = 0
        while len(pq) > 1 and pq[0] < (k):
            heapq.heappush(pq, self.newValue(heapq.heappop(pq), heapq.heappop(pq)))
            count += 1

        return count
