# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while len(set(nums)) != len(nums):
            if len(nums) < 3:
                return count + 1
            else:
                nums = nums[3:]
                count += 1
        return count
