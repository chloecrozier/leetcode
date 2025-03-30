# https://leetcode.com/problems/reverse-degree-of-a-string/description/
class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (i + 1) * (26 - (ord(s[i]) % 97))
        return res
