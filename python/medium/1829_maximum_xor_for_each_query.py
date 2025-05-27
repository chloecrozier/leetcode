# https://leetcode.com/problems/maximum-xor-for-each-query/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] ^= nums[i - 1]
        
        maxVal = pow(2, maximumBit) - 1
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(nums[i] ^ maxVal)
        return res
