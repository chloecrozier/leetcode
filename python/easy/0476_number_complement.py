# https://leetcode.com/problems/number-complement/description/
class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        count = 0
        while num:
            res += (1 ^ (1 & num)) << count
            num = num >> 1
            count += 1
        return res
