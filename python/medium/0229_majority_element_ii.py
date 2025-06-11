# https://leetcode.com/problems/majority-element-ii/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occurences = len(nums) // 3
        m = {}
        res = []

        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
            if m[n] > occurences:
                res.append(n)
                m[n] = -1

        return res
