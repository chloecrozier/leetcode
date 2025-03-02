# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        minIndex = len(s)
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]] = -1
            else:
                m[s[i]] = i

        for key, value in m.items():
            if value != -1:
                minIndex = min(minIndex, value)

        return -1 if minIndex == len(s) else minIndex
