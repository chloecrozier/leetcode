# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        curr = 0
        if len(words) == len(s):
            for w in words:
                if s[curr] != w[0]:
                    return False
                curr += 1
            return True
        return False
