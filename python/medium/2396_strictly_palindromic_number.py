# https://leetcode.com/problems/strictly-palindromic-number/description/
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convertToBaseK(n, k):
            if n == 0:
                return n
            else:
                res = []
                while n:
                    res.append(n % k)
                    n //= k
                return res[::-1]

        for i in range(2, n - 1):
            if convertToBaseK(n, i) != convertToBaseK(n, i)[::-1]:
                return False

        return True
