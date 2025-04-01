# # https://leetcode.com/problems/arranging-coins/description/
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            sumCoins = (mid * (mid + 1)) // 2
            if sumCoins > n:
                r = mid - 1
            else:
                l = mid + 1
        return r
