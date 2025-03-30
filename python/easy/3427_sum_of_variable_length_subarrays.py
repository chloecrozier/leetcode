# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        res = 0 
        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[i - 1])

        for i in range(len(nums)):
            diff = i - nums[i]
            if diff > 0:
                res += prefixSum[i] - prefixSum[diff - 1]
            else:
                res += prefixSum[i]

        return res
