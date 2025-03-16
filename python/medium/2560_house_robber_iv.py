# https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def currSum(val):
            count = 0
            prev = len(nums)
            for i in range(len(nums)):
                if i - 1 != prev and nums[i] <= val:
                    count += 1
                    prev = i
            return count

        l = min(nums)
        r = max(nums)
        while l < r:
            mid = (l + r) // 2
            if currSum(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l
