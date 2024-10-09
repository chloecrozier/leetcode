# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/1416502888/?envType=daily-question&envId=2024-10-09
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lCount = 0
        rCount = 0
        moves = 0
        for c in s:
            if c == '(':
                lCount += 1
            else:
                rCount += 1
            if rCount > lCount:
                moves += 1
                lCount += 1
        return moves + abs(rCount - lCount)
