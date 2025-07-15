# https://leetcode.com/problems/hash-divided-string/description/
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ''
        for i in range(0, len(s) - k + 1, k):
            curr = list(s[i:i + k])
            val = sum(ord(x) - ord('a') for x in curr)
            res += chr(val % 26 + ord('a'))
        return res
