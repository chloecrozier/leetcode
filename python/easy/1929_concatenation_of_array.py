# https://leetcode.com/problems/concatenation-of-array/description/
class Solution(object):
    def getConcatenation(self, nums):
        ans = [0] * (2 * (len(nums)))
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans
