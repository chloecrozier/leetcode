# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/?envType=daily-question&envId=2025-04-03
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pre = [nums[0]] * len(nums)
        post = [nums[0]] * len(nums)
        preMax = nums[0]
        postMax = nums[-1]

        for i in range(len(nums)):
            if nums[i] > preMax:
                preMax = nums[i]
            pre[i] = preMax
            if nums[len(nums) - 1 - i] > postMax:
                postMax = nums[len(nums) - 1 - i]
            post[len(nums) - 1 - i] = postMax

        res = 0
        for i in range(1, len(nums) - 1):
            res = max(res, (pre[i - 1] - nums[i]) * post[i + 1])

        return res
