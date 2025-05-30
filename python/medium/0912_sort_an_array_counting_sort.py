# https://leetcode.com/problems/sort-an-array/description/?envType=problem-list-v2&envId=counting-sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxVal = max(nums)
        minVal = min(nums)
        count = [0] * (abs(maxVal - minVal) + 1)

        for i in range(len(nums)):
            print(nums[i], i, minVal, maxVal, abs(nums[i]) - abs(minVal), nums[i] - minVal)
            count[nums[i] - minVal] += 1

        val = 0
        curr = 0
        while curr < len(nums):
            for i in range(count[val]):
                nums[curr] = val + minVal
                curr += 1
            val += 1
        return nums
