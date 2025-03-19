# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            curr = ""
            for i in range(len(s) - 1):
                curr += str((int(s[i]) + int(s[i + 1])) % 10)
            s = curr
        return s[0] == s[1]
