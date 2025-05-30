# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/?envType=problem-list-v2&envId=counting-sort
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        res = ''
        odd = ''
        for i in range(len(count)):
            if count[i] % 2 == 1:
                odd = chr(i + ord('a'))
            for j in range(0, count[i] // 2):
                res += chr(i + ord('a'))
        
        return res + odd + res[::-1]
