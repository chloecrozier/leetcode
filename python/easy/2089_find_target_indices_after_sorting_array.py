# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=problem-list-v2&envId=binary-search
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        nums = list(set(nums)).sort()
        left = 0
        right = len(nums)
        res = []
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                res.append(mid)
                return res
        return res
