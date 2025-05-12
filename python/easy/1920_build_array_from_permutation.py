# https://leetcode.com/problems/build-array-from-permutation/description/
class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]


# beats 100%
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res
