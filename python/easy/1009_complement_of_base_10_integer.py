# https://leetcode.com/problems/complement-of-base-10-integer/description/
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        count = 0
        while n:
            res += (1 ^ (1 & n)) << count
            n = n >> 1
            count += 1
        return res
