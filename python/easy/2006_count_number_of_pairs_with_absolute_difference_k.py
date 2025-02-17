# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

            if nums[i] - k in m:
                count += m[nums[i] - k]
            if nums[i] + k in m:
                count += m[nums[i] + k]

        return count
