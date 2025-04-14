# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        rCount = 0
        lCount = 0
        for c in s:
            if c == 'R':
                rCount += 1
            else:
                lCount += 1
            if rCount == lCount:
                res += 1
                rCount = 0
                lCount = 0
        return res
