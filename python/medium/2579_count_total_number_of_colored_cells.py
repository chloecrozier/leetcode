# https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05
class Solution:
    def coloredCells(self, n: int) -> int:
        res = 0
        while n > 1:
            res += 4 * (n - 1)
            n -= 1
        return res + 1
