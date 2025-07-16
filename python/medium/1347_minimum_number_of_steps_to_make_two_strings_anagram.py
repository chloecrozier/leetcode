# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sFreq = [0] * 26
        tFreq = [0] * 26
        for c in s:
            sFreq[ord(c) - ord('a')] += 1
        for c in t:
            tFreq[ord(c) - ord('a')] += 1

        res = 0
        for i in range(26):
            if tFreq[i] < sFreq[i]:
                res += sFreq[i] - tFreq[i]
        return res
