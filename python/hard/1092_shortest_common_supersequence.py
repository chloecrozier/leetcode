# https://leetcode.com/problems/shortest-common-supersequence/description/?envType=daily-question&envId=2025-02-28
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        res = ''
        dp = [[''] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        c1 = 0
        c2 = 0
        lcs = dp[-1][-1]
        for c in lcs:
            while c != str1[c1]:
                res += str1[c1]
                c1 += 1
            while c != str2[c2]:
                res += str2[c2]
                c2 += 1
            res += c
            c1 += 1
            c2 += 1
        
        return res + str1[c1:] + str2[c2:]
