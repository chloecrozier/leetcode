# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        long = nums1
        short = nums2
        if len(nums2) > len(nums1):
            long = nums2
            short = nums1

        m = {}
        for n in long:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        res = []
        for n in short:
            if n in m and m[n] > 0:
                m[n] -= 1
                res.append(n)
        return res
