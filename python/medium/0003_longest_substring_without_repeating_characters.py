# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        length = 0
        maxVal = 0
        i = 0
        while i < len(s):
            if s[i] in count:
                i = count[s[i]]
                count = {}
                length = 0
            else:
                count[s[i]] = i
                length += 1
            maxVal = max(maxVal, length)
            i += 1
        return maxVal
