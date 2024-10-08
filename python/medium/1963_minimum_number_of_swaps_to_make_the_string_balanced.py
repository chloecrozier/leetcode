# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/?envType=daily-question&envId=2024-10-08
class Solution:
    def minSwaps(self, s: str) -> int:
        ls = list(s)
        lastOpen = 0
        lastClosed = len(ls) - 1
        openCount = 0
        closedCount = 0
        swaps = 0
        for i in range(len(ls)):
            if ls[i] == '[':
                lastOpen = i
                openCount += 1
            else:
                lastClosed = i
                closedCount += 1
            if closedCount > openCount:
                closedCount -= 1
                openCount += 1
                ls[lastOpen], ls[lastClosed] = ls[lastClosed], ls[lastOpen]
                swaps += 1
        return swaps
