# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10
class Solution:
    def maxDifference(self, s: str) -> int:
        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

        minEven = len(s)
        maxOdd = 1
        for key, val in m.items():
            if val % 2:
                maxOdd = max(maxOdd, val)
            else:
                minEven = min(minEven, val)
        return maxOdd - minEven
