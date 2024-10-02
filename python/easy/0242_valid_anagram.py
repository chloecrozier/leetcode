# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            if t[i] in count:
                count[t[i]] -= 1
            else:
                count[t[i]] = -1
        
        for key, val in count.items():
            if val != 0:
                return False
        return True
