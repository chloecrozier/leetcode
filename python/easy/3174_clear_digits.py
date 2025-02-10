# https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10
class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        s = list(s)
        tracker = []
        for i in range(len(s)):
            if s[i].isdigit():
                if res:
                    res.pop()
            else:
                res.append(s[i])

        return ''.join(res)
