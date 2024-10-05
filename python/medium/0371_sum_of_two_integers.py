# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        count = [0] * 2000
        absCount = []
        if a < 0:
            for i in range(abs(a)):
                count.pop()
        else:
            for i in range(a):
                count.append(0)
        if b < 0:
            for i in range(abs(b)):
                count.pop()
        else:
            for i in range(b):
                count.append(0)
        
        if len(count) <= 2000:
            for i in range(len(count), 2000):
                absCount.append(0)
            return len(absCount) * -1
        else:
            for i in range(2000):
                count.pop()
            return len(count)
