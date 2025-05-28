# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def maxSum(self, m: List[List[int]]) -> int:
        maxVal = 0
        for i in range(len(m) - 2):
            for j in range(len(m[i]) - 2):
                currSum = m[i][j] + m[i][j + 1] + m[i][j + 2] + m[i + 1][j + 1] + m[i + 2][j] + m[i + 2][j + 1] + m[i + 2][j + 2]
                maxVal = max(maxVal, currSum)
        return maxVal
