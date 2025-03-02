# https://leetcode.com/problems/longest-common-subsequence/submissions/1559754309/
class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
