# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff1 = ''
        diff2 = ''
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff1 and diff2:
                    if diff1 != s2[i] or diff2 != s1[i]:
                        return False
                else:
                    diff1 = s1[i]
                    diff2 = s2[i]
                count += 1
            if count > 2:
                return False
                
        return count == 2
