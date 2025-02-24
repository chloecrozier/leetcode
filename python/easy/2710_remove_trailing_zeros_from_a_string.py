# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        endNum = len(num)
        while num[-1] == '0':
            endNum -= 1
            num = num[0:endNum]
        return num
