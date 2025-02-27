# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        m = {}
        dp = [[0] * len(arr) for _ in range(len(arr))]
        maxVal = 0

        for i in range(len(arr)):
            m[arr[i]] = i

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                firstNum = arr[j] - arr[i] # order in subseq: firstNum i j
                if firstNum in m and m[firstNum] < i:
                    dp[i][j] = dp[m[firstNum]][i] + 1
                    maxVal = max(maxVal, dp[i][j])

        return maxVal + 2 if maxVal else maxVal
