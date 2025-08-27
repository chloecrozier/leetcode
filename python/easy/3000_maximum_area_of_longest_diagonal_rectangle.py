# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26
class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        area = 0
        diag = 0
        for i in range(len(d)):
            currArea = d[i][0] * d[i][1]
            currDiag = sqrt((d[i][0] * d[i][0]) + (d[i][1] * d[i][1]))
            if currDiag > diag:
                area = currArea
                diag = currDiag
            elif currDiag == diag:
                area = max(area, currArea)
        return area
