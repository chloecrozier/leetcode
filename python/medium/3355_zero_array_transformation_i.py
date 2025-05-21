# https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
            diff = [0] * (len(nums) + 1)
            for l, r in queries:
                diff[l] += 1
                diff[r + 1] -= 1

            for i in range(1, len(nums)):
                diff[i] += diff[i - 1]

            for i in range(len(nums)):
                if diff[i] < nums[i]:
                    return False
            return True
