# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]
        prev = nums[0]
        i = 1
        while prev < nums[i]:
            prev = nums[i]
            i += 1
        return nums[i]
