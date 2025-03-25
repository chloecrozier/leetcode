# https://leetcode.com/problems/smallest-range-ii/description/
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[i + 1] - k, nums[0] + k)

            minDiff = min(minDiff, high - low)

        return minDiff
