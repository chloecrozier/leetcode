# https://leetcode.com/problems/zero-array-transformation-ii/description/?envType=daily-question&envId=2025-03-13
class Solution:
    def isZeroArray(self, nums, q, length):
        diff = [0] * (len(nums) + 1)
        for i in range(length):
            diff[q[i][0]] += q[i][2]
            diff[q[i][1] + 1] -= q[i][2]

        curr = 0
        for i in range(len(nums)):
            curr += diff[i]
            if nums[i] - curr > 0:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        count = 0
        l = 0
        r = len(queries)
        if not self.isZeroArray(nums, queries, r):
            return -1

        while l < r:
            mid = ((r - l) // 2) + l
            if self.isZeroArray(nums, queries, mid):
                r = mid
            else:
                l = mid + 1
        return r
