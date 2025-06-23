# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
class Solution:
    def maxFreqSum(self, s: str) -> int:
        m = {}
        maxVowel = 0
        maxCons = 0
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        for key, val in m.items():
            if key in ['a', 'e', 'i', 'o', 'u']:
                maxVowel = max(maxVowel, val)
            else:
                maxCons = max(maxCons, val)
        return maxVowel + maxCons
