# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07
class Solution:
    def minLength(self, s: str) -> int:
        prevLen = len(s)
        notDone = True
        while notDone:
            s = s.replace('AB', '')
            s = s.replace('CD', '')
            if prevLen == len(s):
                notDone = False
            else:
                prevLen = len(s)
        return len(s)
