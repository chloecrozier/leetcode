# https://leetcode.com/problems/xor-operation-in-an-array/description/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(start, start + (2 * n), 2):
            res = res ^ i
        return res
