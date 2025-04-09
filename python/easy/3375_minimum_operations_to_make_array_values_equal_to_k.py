# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        setNums = set(nums)
        if k > min(nums):
            return -1

        if k in setNums:
            return len(setNums) - 1
        else:
            return len(setNums)
