# https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            sum = 0
            prev2 = 0
            prev1 = 0
            for i in range(len(nums)):
                sum = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = sum
            return sum
