# https://leetcode.com/problems/build-array-from-permutation/description/
class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
