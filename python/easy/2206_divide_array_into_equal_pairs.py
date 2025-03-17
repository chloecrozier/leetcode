# https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = [0] * (max(nums) + 1)
        for n in nums:
            count[n] += 1

        for n in count:
            if n % 2:
                return False

        return True
