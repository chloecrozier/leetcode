# https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = {}
        maxVal = pow(2, len(nums)) - 1
        minVal = maxVal

        for string in nums:
            seen[int(string, 2)] = 1

        for i in range(0, maxVal):
            if i not in seen:
                minVal = min(minVal, i)
                return f"{minVal:0{len(nums)}b}"

        return maxVal
