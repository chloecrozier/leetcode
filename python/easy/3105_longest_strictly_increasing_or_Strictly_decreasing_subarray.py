# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        count = 1
        maxVal = -1
        isIncreasing = True

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if not isIncreasing:
                    isIncreasing = True
                    count = 2
                else:
                    count += 1
            elif nums[i - 1] > nums[i]:
                if isIncreasing:
                    isIncreasing = False
                    count = 2
                else:
                    count += 1
            else:
                count = 1

            maxVal = max(maxVal, count)

        return maxVal
