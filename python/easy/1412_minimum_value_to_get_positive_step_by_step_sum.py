# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        minVal = min(nums)
        return 1 if minVal >= 1 else abs(minVal) + 1
