# https://leetcode.com/problems/valid-palindrome-ii/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if s[l + 1:r + 1] == s[l + 1:r + 1][::-1]:
                    return True
                elif s[l:r] == s[l:r][::-1]:
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return True
