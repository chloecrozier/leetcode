# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for num in nums[max(0, i - nums[i]):i + 1]:
                res += num
        return res
