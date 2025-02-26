# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-02-26
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxVal = nums[0]
        minVal = nums[0]
        currMin = nums[0]
        currMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            maxVal = max(maxVal, currMax)
            currMin = min(currMin + nums[i], nums[i])
            minVal = min(minVal, currMin)

        return max(abs(minVal), maxVal)
