# https://leetcode.com/problems/find-common-elements-between-two-arrays/description/
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = 0
        n2 = 0
        set1 = set(nums1)
        set2 = set(nums2)
        for n in nums1:
            if n in set2:
                n1 += 1
        for n in nums2:
            if n in set1:
                n2 += 1
        return [n1, n2]
