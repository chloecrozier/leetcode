# https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2025-08-01
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def getNextRow(prev):
            row = [1]
            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i + 1])
            row.append(1)
            return row

        triangle = [[1]]
        for i in range(numRows - 1):
            triangle.append(getNextRow(triangle[i]))
        return triangle
