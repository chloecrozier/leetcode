# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxVal = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] > nums[j]:
                    for z in range(j + 1, len(nums)):
                        maxVal = max(maxVal, (nums[i] - nums[j]) * nums[z])
        return maxVal
