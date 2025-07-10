# https://leetcode.com/problems/a-number-after-a-double-reversal/submissions/1692827536/
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        digits = list(str(num))
        while digits[-1] == '0' and len(digits) > 1:
            digits.pop()
        return int(''.join(digits)) == num
