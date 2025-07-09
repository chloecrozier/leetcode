# https://leetcode.com/problems/replace-all-digits-with-characters/description/
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(0, len(s) - 1, 2):
            s[i + 1] = chr(ord(s[i]) + int(s[i + 1]))
        return ''.join(s)
