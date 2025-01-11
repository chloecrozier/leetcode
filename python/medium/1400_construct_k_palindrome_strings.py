# https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-11
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        odd = 0
        even = 0
        for key, value in letters.items():
            if value % 2:
                odd += 1
            else:
                even += 1
    
        if len(s) < k or odd > k:
            return False

        return True
