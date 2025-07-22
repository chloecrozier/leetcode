# https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = l + 1
        m = {nums[l]: l}
        currSum = nums[l]
        res = currSum
        while l < r and r < len(nums):
            while nums[r] in m:
                currSum -= nums[l]
                del m[nums[l]]
                l += 1
            else:
                currSum += nums[r]
                m[nums[r]] = r
                r += 1
            res = max(res, currSum)

        return res
