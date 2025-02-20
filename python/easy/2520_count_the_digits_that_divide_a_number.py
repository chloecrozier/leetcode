# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        count = 0
        for n in digits:
            if num / n == num // n:
                count += 1
        return count
