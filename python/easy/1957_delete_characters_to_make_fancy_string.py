# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2025-01-14
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        count = 1
        last = s[0]
        res = s[0]
        for i in range(1, len(s)):
            if s[i] == last:
                count += 1
                if count < 3:
                    res += s[i]
            else:
                last = s[i]
                count = 1
                res += s[i]

        return res
