# https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution(object):
    def runningSum(self, nums):
        ans = [nums[0]] * len(nums)
        for i in range (1, len(nums)):
                ans[i] = nums[i] + ans[i-1]
        return ans
