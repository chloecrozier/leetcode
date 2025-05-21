# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        l = 0
        r = 1
        minLen = len(nums) + 1

        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target:
                minLen = min(minLen, r - l)
                currSum -= nums[l]
                l += 1
            r += 1
        
        return 0 if minLen == len(nums) + 1 else minLen
