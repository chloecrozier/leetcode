# https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = l + 1

        res = 0
        curr = []
        while l < r and r <= len(nums):
            curr = nums[l:r]
            if len(set(curr)) == len(curr):
                r += 1
                res = max(res, sum(curr))
            else:
                l += 1
        return res
