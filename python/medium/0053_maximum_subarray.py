# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
        return maxSum
