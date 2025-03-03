# https://leetcode.com/problems/degree-of-an-array/description/
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        maxFreq = 0
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
            maxFreq = max(maxFreq, m[n])
        

        freqItems = {}
        for i in range(len(nums)):
            if m[nums[i]] == maxFreq:
                if nums[i] in freqItems:
                    freqItems[nums[i]][1] = i
                else:
                    freqItems[nums[i]] = [i, len(nums) - 1]
        
        minDiff = len(nums)
        for key, val in freqItems.items():
            minDiff = min(minDiff, val[1] - val[0] + 1)

        return minDiff if minDiff else 1
