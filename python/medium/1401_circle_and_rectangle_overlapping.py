# https://leetcode.com/problems/circle-and-rectangle-overlapping/description/
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def getDist(a1, b1, a2, b2):
            return math.sqrt((a1 - a2)**2 + (b1 - b2)**2)

        if xCenter >= x1 and xCenter <= x2 and yCenter >= y1 and yCenter <= y2:
                return True

        minDist = radius + 1
        for i in range(x1, x2 + 1):
            dist = min(getDist(i, y1, xCenter, yCenter), getDist(i, y2, xCenter, yCenter))
            if dist <= minDist:
                minDist = dist
                if minDist <= radius:
                    return True
        for i in range(y1, y2 + 1):
            dist = min(getDist(x1, i, xCenter, yCenter), getDist(x2, i, xCenter, yCenter))
            if dist <= minDist:
                minDist = dist
                if minDist <= radius:
                    return True

        return False
