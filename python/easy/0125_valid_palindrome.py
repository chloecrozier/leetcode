# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while (not s[l].isalnum()) and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                print(f"{s[l].upper()}, {s[r].upper()}")
                l += 1
                r -= 1
        return True
