# https://leetcode.com/problems/perfect-number/description/
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        sum = 1
        minNum = num
        for i in range(2, (num // 2)):
            if i >= minNum:
                break
            if (num // i) == (num / i):
                sum += i
                sum += num // i
                minNum = min(minNum, num // i)
            if sum > num:
                return False

        if sum == num:
            return True

        return False
