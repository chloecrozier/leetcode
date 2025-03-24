https://leetcode.com/problems/count-days-without-meetings/description/?envType=daily-question&envId=2025-03-24
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        start = meetings[0][0]
        end = meetings[0][1]
        merged = []
        for meeting in meetings:
            overlapStart = meeting[0] <= start and meeting[1] >= start
            overlapEnd = meeting[1] >= end and meeting[0] <= end
            inbetween = meeting[0] >= start and meeting[1] <= end
            if overlapStart or overlapEnd or inbetween:
                start = min(start, meeting[0])
                end = max(end, meeting[1])
            else:
                merged.append([start, end])
                start = meeting[0]
                end = meeting[1]
        if not merged or (merged[-1][0] != start and merged[-1][1] != end):
            merged.append([start, end])

        missingDays = days
        for times in merged:
            missingDays -= times[1] - times[0] + 1

        return missingDays
