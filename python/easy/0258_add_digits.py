# https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res > 9:
            res = sum([int(n) for n in str(res)])
        return res
