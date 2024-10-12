# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/?envType=daily-question&envId=2024-10-12
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        count = 0

        for interval in intervals:
            heapq.heappush(start, interval[0])
            heapq.heappush(end, interval[1])

        while start:
            i = heapq.heappop(start)
            if end[0] < i:
                heapq.heappop(end)
            else:
                count += 1

        return count
