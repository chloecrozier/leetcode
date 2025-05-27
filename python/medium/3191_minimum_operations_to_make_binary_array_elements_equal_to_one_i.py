# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                nums[i + 1] = (nums[i + 1] + 1) % 2
                nums[i + 2] = (nums[i + 2] + 1) % 2
                nums[i] = 1
                res += 1

        if nums[i+1] + nums[i+2] == 2:
            return res
        else:
            return -1
