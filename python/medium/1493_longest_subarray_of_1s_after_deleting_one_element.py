# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        if len(zeros) <= 1:
            return len(nums) - 1
        else:
            diff = 0
            for i in range(len(zeros) - 2):
                diff = max(diff, zeros[i + 2] - zeros[i] - 2)
            diff = max(diff, len(nums) - zeros[-2] - 2)
            diff = max(diff, zeros[1] - 1)
            return diff
