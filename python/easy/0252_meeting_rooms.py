# https://leetcode.com/problems/meeting-rooms/description/
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True
