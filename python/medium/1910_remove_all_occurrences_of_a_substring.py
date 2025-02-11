# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            index = s.find(part)
            s = s[0:index] + s[index + len(part):]
        return s
