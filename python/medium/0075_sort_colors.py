# https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                if i != start:
                    nums[i], nums[start] = nums[start], nums[i]
                    start += 1
                    i -= 1
            elif nums[i] == 2:
                if i != end:
                    nums[i], nums[end] = nums[end], nums[i]
                    end -= 1
                    i -= 1
            i += 1
        return nums
