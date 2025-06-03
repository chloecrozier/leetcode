# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                res += increment
        return res
