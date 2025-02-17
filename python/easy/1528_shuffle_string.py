# https://leetcode.com/problems/shuffle-string/description/
class Solution:
    def restoreString(self, s: str, pos: List[int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[pos[i]] = s[i]
        return "".join(res)
