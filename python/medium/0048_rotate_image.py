# https://leetcode.com/problems/rotate-image/description/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(len(matrix)):
            i = 0
            j = len(matrix) - 1
            while i <= j:
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
                i += 1
                j -= 1
