# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        res = 0
        while i < len(nums) - 1:
            left = i - 1
            right = i + 1
            while left > 0 and nums[i] == nums[left]:
                left -= 1
            while right < len(nums) - 1 and nums[i] == nums[right]:
                right += 1
            
            if nums[i] < nums[left] and nums[i] < nums[right]:
                res += 1
                i = right
            elif nums[i] > nums[left] and nums[i] > nums[right]:
                res += 1
                i = right
            else:
                i += 1

        return res
