# https://leetcode.com/problems/partition-labels/description/?envType=daily-question&envId=2025-03-30
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        intervals = []
        res = []

        for i in range(len(s)):
            if s[i] in m:
                m[s[i]][1] = i
            else:
                m[s[i]] = [i,i]

        for key, val in m.items():
            intervals.append(val)

        # Merged intervals sub-problem
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        merged = []
        for interval in intervals:
            one = (interval[0] <= start and interval[1] >= start)
            two = (interval[1] >= end and interval[0] <= end)
            if (interval[0] <= start and interval[1] >= start) or (interval[1] >= end and interval[0] <= end) or (interval[0] >= start and interval[1] <= end):
                start = min(start, interval[0])
                end = max(end, interval[1])
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
        if not merged or (merged[-1][0] != start and merged[-1][1] != end):
            merged.append([start, end])

        for start, end in merged:
            res.append(end - start + 1)

        return res
