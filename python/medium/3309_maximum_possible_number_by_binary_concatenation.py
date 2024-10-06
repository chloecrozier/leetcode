# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/description/
class Solution:
    def getLength(self, num):
        length = 0
        while num:
            length += 1
            num = num >> 1
        return length

    def calculateCombo(self, n1, n2, n3):
        res = n1
        res = res << self.getLength(n2)
        res = res | n2

        res = res << self.getLength(n3)
        res = res | n3
        return res

    def maxGoodNumber(self, nums: List[int]) -> int:
        res = -1
        x = nums[0]
        y = nums[1]
        z = nums[2]
        res = max(self.calculateCombo(x, y, z), self.calculateCombo(x, z, y), res)
        res = max(self.calculateCombo(y, x, z), self.calculateCombo(y, z, x), res)
        res = max(self.calculateCombo(z, x, y), self.calculateCombo(z, y, x), res)

        return res
