# https://leetcode.com/problems/count-number-of-bad-pairs/description/?envType=daily-question&envId=2025-02-09
class Solution:
#     def countBadPairs(self, nums: List[int]) -> int:
#         goodCount = 0
#         total = ((len(nums) - 1) * len(nums)) // 2
#         m = {}
#         for i in range(len(nums)):
#             if nums[i] - i in m:
#                 m[nums[i] - i] += 1
#             else:
#                 m[nums[i] - i] = 1

#         for key, value in m.items():
#             if value >= 2:
#                 goodCount += (value * (value - 1)) // 2

#         return total - goodCount

    def countBadPairs(self, nums: List[int]) -> int:
        m = {}
        badPairs = 0
        for i in range(len(nums)):
            if nums[i] - i in m:
                badPairs += i - m[nums[i] - i]
                m[nums[i] - i] += 1
            else:
                badPairs += i
                m[nums[i] - i] = 1

        return badPairs
