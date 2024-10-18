# https://leetcode.com/problems/plus-one/description/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] = digits[-1] + 1
        if digits[-1] <= 9:
            return digits
        else:
            for i in range(len(digits) - 1, -1, -1):
                digits[i] = digits[i] + carry
                if digits[i] > 9:
                    digits[i] = digits[i] % 9 - 1
                    if i == 0:
                        digits.insert(0, 1)
                    else:
                        carry = 1
                else:
                    carry = 0
            return digits
