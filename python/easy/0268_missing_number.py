# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = 0
        actualSum = 0
        for i in range(len(nums)):
            expectedSum += i
            actualSum += nums[i]
        expectedSum += len(nums)
        return expectedSum - actualSum
