class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        mask = 0
        maxLen = 0
        curr = 0

        for i in range(len(s)):
            if s[i] == 'a':
                mask ^= 1
            elif s[i] == 'e':
                mask ^= 2
            elif s[i] == 'i':
                mask ^= 4
            elif s[i] == 'o':
                mask ^= 8
            elif s[i] == 'u':
                mask ^= 16
        
            print(s[i], mask, bin(mask))
            if mask == 0:
                curr += 1
                maxLen = max(maxLen, curr)
            else:
                curr = 0

        return maxLen
