# https://leetcode.com/problems/maximum-length-of-repeated-subarray/solutions/
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxVal = 0
        dp = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxVal = max(maxVal, dp[i][j])
        return maxVal

        # TOO SLOW
        # maxVal = 0
        # subs = set()
        # for i in range(len(nums1)):
        #     for j in range(len(nums1) - i):
        #         subs.add(tuple(nums1[i:i + j + 1]))
        # for i in range(len(nums2)):
        #     for j in range(len(nums2) - i):
        #         if tuple(nums2[i:i + j + 1]) in subs:
        #             maxVal = max(maxVal, len(nums2[i:i + j + 1]))
        # return maxVal
