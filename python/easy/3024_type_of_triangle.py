# https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if max(nums) < sum(nums) - max(nums):
            if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
                if nums[0] == nums[1] and nums[0] == nums[2]:
                    return "equilateral"
                else:
                    return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
