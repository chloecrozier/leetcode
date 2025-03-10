# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        res = []
        for n in nums:
            count[n - 1] += 1

        for i in range(len(count)):
            if count[i] == 0:
                res.append(i + 1)
        return res
