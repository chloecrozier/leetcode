# https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = {}
        for i in range(len(t)):
            if i == len(t) - 1:
                if t[i] in m:
                    m[t[i]] -= 1
                else:
                    return t[i]
            else:
                if s[i] in m:
                    m[s[i]] += 1
                else:
                    m[s[i]] = 1

                if t[i] in m:
                    m[t[i]] -= 1
                else:
                    m[t[i]] = -1

        for key, val in m.items():
            if val == -1:
                return key
