# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        indexMap = {}
        for i in range(len(nums)):
            if nums[i] not in indexMap:
                indexMap[nums[i]] = i
            if target - nums[i] in indexMap and i != indexMap[target - nums[i]]:
                    res = [indexMap[target - nums[i]], i]
                    break
        return res
