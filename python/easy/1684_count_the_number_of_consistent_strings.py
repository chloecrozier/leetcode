# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for s in words:
            count = 0
            for c in allowed:
                count += s.count('a')
                res += 1
        return res
