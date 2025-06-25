# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)

        res = []
        even = True
        while pos and neg:
            if even:
                res.append(pos.pop(0))
                even = False
            else:
                res.append(neg.pop(0))
                even = True
        while neg:
            res.append(neg.pop(0))

        return res
