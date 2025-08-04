class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                m[i + 1][j + 1] = matrix[i][j] + m[i + 1][j] + m[i][j + 1] - m[i][j]
                maxSum = max(maxSum, m[i + 1][j + 1])
        
        if maxSum == k:
            return k
        

        for i in range(1, len(m)):
            for j in range(i, len(m[i])):
                currSum = m[i][j] - m[i - 1][j] - m[i][j - 1] + m[i - 1][j- 1]

        return currSum
