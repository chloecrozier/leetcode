# https://leetcode.com/problems/maximum-width-ramp/solutions/5893635/fastest-way-to-solve-maximum-width-ramp/?envType=daily-question&envId=2024-10-10
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxW = 0
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                maxW = max(maxW, j - stack.pop())
        return maxW
