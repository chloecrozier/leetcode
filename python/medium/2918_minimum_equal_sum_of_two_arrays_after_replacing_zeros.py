# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        z1 = nums1.count(0)
        s2 = sum(nums2)
        z2 = nums2.count(0)

        if ((s1 + z1 > s2) and z2 == 0) or ((s2 + z2 > s1) and z1 == 0):
            return -1
        else:
            return max(s1 + z1, s2 + z2)
