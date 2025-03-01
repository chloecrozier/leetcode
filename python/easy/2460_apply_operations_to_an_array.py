# https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        lastZero = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                nums[i], nums[lastZero] = nums[lastZero], nums[i]
                lastZero += 1

        if nums[-1] != 0:
                nums[-1], nums[lastZero] = nums[lastZero], nums[-1]

        return nums
