# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxVol = -1
        while l <= r:
            vol = min(heights[l], heights[r]) * (r - l)
            maxVol = max(maxVol, vol)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxVol
