# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/?envType=daily-question&envId=2025-05-27class Solution:
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if i % m == 0:
                res -= i
            else:
                res += i
        return res
