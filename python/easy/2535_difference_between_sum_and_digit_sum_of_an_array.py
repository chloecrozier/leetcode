# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        digitSum = 0
        digits = ''.join([str(x) for x in nums])
        for i in range(len(digits)):
            digitSum += int(digits[i])
        return abs(totalSum - digitSum)
