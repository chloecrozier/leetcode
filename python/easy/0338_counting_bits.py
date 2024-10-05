# https://leetcode.com/problems/counting-bits/description/
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        res[0] = 0
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
