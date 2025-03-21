# https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maxCount = 1
        curr = 0
        l = 0
        for r in range(len(nums)):
            while curr & nums[r] != 0:
                curr = curr ^ nums[l]
                l += 1
            curr = curr | nums[r]
            maxCount = max(maxCount, r - l + 1)

        return maxCount
