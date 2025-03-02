# https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[0])
        for i in range(1, len(t)):
            res += ord(t[i]) - ord(s[i - 1])
        return chr(res)
