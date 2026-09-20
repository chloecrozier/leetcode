# https://leetcode.com/problems/reverse-degree-of-a-string/description/
class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (i + 1) * (26 - (ord(s[i]) % 97))
        return res



# Redone a year because I forgot I already did it until re-submitting to github
# Redone because it was the probelm fo the day too. I imporved by not using 97 as a magic number
# https://leetcode.com/problems/reverse-degree-of-a-string/description/?envType=daily-question&envId=2026-09-20
class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for i in range(len(s)):
            degree += (26 - (ord(s[i]) - ord('a'))) * (i + 1)
        return degree
