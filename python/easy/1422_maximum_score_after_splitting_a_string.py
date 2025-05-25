# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def maxScore(self, s: str) -> int:
        ones = [0] * len(s)
        totalOnes = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                totalOnes += 1
            ones[i] += totalOnes
            
        maxVal = 0
        currZeros = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                currZeros += 1
            maxVal = max(maxVal, currZeros + ones[i + 1])
        return maxVal
