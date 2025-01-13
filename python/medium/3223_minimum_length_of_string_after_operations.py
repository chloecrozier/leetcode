# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/?envType=daily-question&envId=2025-01-13
class Solution:
    def minimumLength(self, s: str) -> int:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
                if count[c] > 2:
                    count[c] -= 2
            else:
                count[c] = 1
        
        return sum(count.values())
