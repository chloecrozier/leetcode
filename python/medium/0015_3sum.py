# https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        prev = nums[0]
        for i in range(0, len(nums)):
            x = nums[i]
            if prev != x or i == 0:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    y = nums[left]
                    z = nums[right]
                    if x + y + z == 0:
                        res.append([x, y, z])
                        while y == nums[left] and left < right:
                            left += 1
                    elif x + y + z < 0:
                        left += 1
                    else:
                        right -= 1
            prev = x
        return res
