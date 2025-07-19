# https://leetcode.com/problems/count-asterisks/description/
class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        res = 0
        for i in range(0, len(s), 2):
            res += s[i].count('*')
        return res
