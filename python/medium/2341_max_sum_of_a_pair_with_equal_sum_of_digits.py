# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12
class Solution:
    def sumDigits(self, num):
        digitSum = 0
        while num > 0:
            digitSum += num % 10
            num //= 10
        return digitSum

    def maximumSum(self, nums: List[int]) -> int:
        maxVal = -1
        m = {}
        for i in range(len(nums)):
            sum1 = self.sumDigits(nums[i])
            if sum1 in m:
                heapq.heappush(m[sum1], -nums[i])
            else:
                m[sum1] = [-nums[i]]

        for key, value in m.items():
            if len(value) >= 2:
                maxVal = max(maxVal, abs(heapq.heappop(value) + heapq.heappop(value)))

        return maxVal
