# https://leetcode.com/problems/smallest-range-i/description/
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - (2 * k), 0)
