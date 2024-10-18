# https://leetcode.com/problems/minimum-time-difference/description/
class Solution:
    def calcDiff(self, s1, s2) -> int:
        h1, m1 = map(int, s1.split(':'))
        h2, m2 = map(int, s2.split(':'))
        return m2 - m1 + (60 * (h2 - h1))

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        print(timePoints)
        minTime = 1440
        for i in range(0, len(timePoints) - 1):
            if timePoints[i] == timePoints[i + 1]:
                return 0
            else:
                minTime = min(minTime, self.calcDiff(timePoints[i], timePoints[i + 1]))
        minTime = min(minTime, self.calcDiff(timePoints[0], timePoints[-1]), abs(1440 - self.calcDiff(timePoints[0], timePoints[-1])))
        return minTime
