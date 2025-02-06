# https://leetcode.com/problems/tuple-with-same-product/description/?envType=daily-question&envId=2025-02-06
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = nums[i] * nums[j]
                if val in m:
                    m[val] += 1
                else:
                    m[val] = 1

        for key, val in m.items():
            if val >= 2:
                res += math.comb(val, 2) * 8
        return res
