class Solution:
    def getSum(self, x, y, z, w):
        return ((10 * x) + y) + ((10 * z) + w)

    def minimumSum(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        return self.getSum(num[0], num[2], num[1], num[3])
