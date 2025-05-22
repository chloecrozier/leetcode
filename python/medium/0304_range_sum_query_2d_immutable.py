# https://leetcode.com/problems/range-sum-query-2d-immutable/description/?envType=problem-list-v2&envId=prefix-sum
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.m[i + 1][j + 1] = matrix[i][j] + self.m[i][j + 1] + self.m[i + 1][j] - self.m[i][j] 

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.m[r2 + 1][c2 + 1] - self.m[r1][c2 + 1] - self.m[r2 + 1][c1] + self.m[r1][c1]
