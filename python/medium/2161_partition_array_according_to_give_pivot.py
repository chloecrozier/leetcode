# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre = []
        pivots = []
        post = []
        for n in nums:
            if n < pivot:
                pre.append(n)
            elif n == pivot:
                pivots.append(n)
            else:
                post.append(n)
        return pre + pivots + post
