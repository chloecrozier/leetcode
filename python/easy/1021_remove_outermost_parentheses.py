# https://leetcode.com/problems/remove-outermost-parentheses/description/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left = 0
        right = 0
        res = ""
        curr = ""
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
                
            curr += c
            if left == right:
                res += curr[1:-1]
                curr = ""

        return res
