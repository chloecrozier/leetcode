# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        maxSum = curr
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += nums[i]
            else:
                curr = nums[i]
            maxSum = max(maxSum, curr)
        return maxSum
