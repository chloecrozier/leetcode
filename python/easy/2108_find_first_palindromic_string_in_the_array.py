# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == ''.join(reversed(w)):
                return w
        return ''
