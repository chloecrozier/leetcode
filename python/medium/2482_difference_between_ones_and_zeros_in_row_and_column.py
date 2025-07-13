# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = [0] * len(grid)
        onesCol = [0] * len(grid[0])

        for i in range(len(grid)):
            onesRow[i] = sum(grid[i])
        for j in range(len(grid[0])):
            onesCol[j] = sum(row[j] for row in grid)

        res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                zerosRow = len(res) - onesRow[i]
                zerosCol = len(res[0]) - onesCol[j]
                res[i][j] = onesRow[i] + onesCol[j] - zerosRow - zerosCol
        return res
