# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sublist = nums[0:i] + nums[i + 1:]
            if sublist == sorted(set(sublist)):
                return True
        return False
