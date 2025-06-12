# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            maxDiff = max(maxDiff, abs(nums[i] - nums[i + 1]))
        return maxDiff
