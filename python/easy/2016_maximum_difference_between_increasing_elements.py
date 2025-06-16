# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/?envType=daily-question&envId=2025-06-16
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minVals = [-1] * len(nums)
        minVals[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < minVals[i - 1]:
                minVals[i] = nums[i]
            else:
                minVals[i] = minVals[i - 1]

        maxVal = -1
        for i in range(1, len(nums)):
            if minVals[i] < nums[i]:
                maxVal = max(maxVal, nums[i] - minVals[i])

        return maxVal
