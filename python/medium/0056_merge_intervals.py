#x
# https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for interval in intervals:
            one = (interval[0] <= start and interval[1] >= start)
            two = (interval[1] >= end and interval[0] <= end)
            if (interval[0] <= start and interval[1] >= start) or (interval[1] >= end and interval[0] <= end) or (interval[0] >= start and interval[1] <= end):
                start = min(start, interval[0])
                end = max(end, interval[1])
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
        if not res or (res[-1][0] != start and res[-1][1] != end):
            res.append([start, end])
        return res
