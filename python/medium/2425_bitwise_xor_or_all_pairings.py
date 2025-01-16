# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=daily-question&envId=2025-01-16
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        elif len(nums1) % 2 == 0:
            res = 0
            for n in nums1:
                res = res ^ n
            return res
        elif len(nums2) % 2 == 0:
            res = 0
            for n in nums2:
                res = res ^ n
            return res
        else:
            res = 0
            for n in nums1:
                res = res ^ n
            for n in nums2:
                res = res ^ n
            return res
