# https://leetcode.com/problems/intersection-of-multiple-arrays/description/
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        m = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                curr = nums[i][j]
                if curr in m:
                    m[curr] += 1
                else:
                    m[curr] = 1
        
        res = []
        for key, val in m.items():
            if val == len(nums):
                res.append(key)

        return sorted(res)
