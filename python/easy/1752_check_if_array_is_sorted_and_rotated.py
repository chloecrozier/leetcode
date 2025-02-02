# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02
class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True

        curr = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                curr = i
                break

        return nums[curr:] + nums[:curr] == sorted(nums)
