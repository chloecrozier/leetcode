# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-21
class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i in rows or j in cols:
                    m[i][j] = 0
